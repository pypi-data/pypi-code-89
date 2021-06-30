# Copyright 2019 The Forte Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from collections import defaultdict
from typing import (
    DefaultDict,
    Dict,
    List,
    Set,
    Type,
    Hashable,
    Generic,
    Iterable,
    Tuple,
    KeysView,
)

from sortedcontainers import SortedSet

from forte.common.exception import PackIndexError
from forte.data.ontology.core import GroupType, LinkType, EntryType

logger = logging.getLogger(__name__)


class BaseIndex(Generic[EntryType]):
    r"""A set of indexes used in :class:`BasePack`:

    #. :attr:`entry_index`, the index from each tid to the corresponding entry
    #. :attr:`type_index`, the index from each type to the entries of
       that type
    #. :attr:`link_index`, the index from child
       (:attr:`link_index["child_index"]`)and parent
       (:attr:`link_index["parent_index"]`) nodes to links
    #. :attr:`group_index`, the index from group members to groups.

    """

    def __init__(self):
        # List of basic indexes (switches always on).

        # Mapping from entry's tid to entry type.
        self._entry_index: Dict[int, EntryType] = dict()

        # Mapping from entry's type to entries' id.
        self._type_index: DefaultDict[Type, SortedSet[int]] = defaultdict(
            SortedSet
        )

        # List of other indexes (built when first looked up).
        self._group_index: DefaultDict[Hashable, SortedSet[int]] = defaultdict(
            SortedSet
        )

        self._link_index: Dict[str, DefaultDict[Hashable, SortedSet]] = dict()

        # Indexing switches.
        self._group_index_switch = False
        self._link_index_switch = False

    def update_basic_index(self, entries: List[EntryType]):
        r"""Build or update the basic indexes, including

        (1) :attr:`entry_index`,
        the index from each `tid` to the corresponding entry;

        (2) :attr:`type_index`, the index from each type to the entries of that
        type;

        (3) :attr:`component_index`, the index from each component to the
        entries generated by that component.

        Args:
            entries (list): a list of entries to be added into the basic index.
        """
        for entry in entries:
            self._entry_index[entry.tid] = entry
            self._type_index[type(entry)].add(entry.tid)

    def get_entry(self, tid: int) -> EntryType:
        return self._entry_index[tid]

    def indexed_types(self) -> KeysView[Type]:
        return self._type_index.keys()

    def query_by_type(self, t: Type) -> SortedSet:
        return self._type_index[t]

    def iter_type_index(self) -> Iterable[Tuple[Type, Set[int]]]:
        for t, ids in self._type_index.items():
            yield t, ids

    def remove_entry(self, entry: EntryType):
        self._entry_index.pop(entry.tid)
        self._type_index[type(entry)].remove(entry.tid)

        self.turn_group_index_switch(on=False)
        self.turn_link_index_switch(on=False)

    @property
    def link_index_on(self):
        return self._link_index_switch

    def turn_link_index_switch(self, on: bool):
        self._link_index_switch = on

    @property
    def group_index_on(self):
        return self._group_index_switch

    def turn_group_index_switch(self, on: bool):
        self._group_index_switch = on

    def build_link_index(self, links: List[LinkType]):
        r"""Build the :attr:`link_index`, the index from child and parent nodes
        to links. It will build the links with the links in the dataset.

        :attr:`link_index` consists of two sub-indexes:
        "child_index" is the index from child nodes to their corresponding
        links, and "parent_index" is the index from parent nodes to their
        corresponding links.
        Returns:

        """
        self.turn_link_index_switch(on=True)
        self._link_index["child_index"] = defaultdict(set)
        self._link_index["parent_index"] = defaultdict(set)
        self.update_link_index(links)

    def build_group_index(self, groups: List[GroupType]):
        r"""Build :attr:`group_index`, the index from group members to groups.

        Returns:

        """
        self.turn_group_index_switch(on=True)
        self._group_index = defaultdict(set)
        self.update_group_index(groups)

    def link_index(self, tid: int, as_parent: bool = True) -> Set[int]:
        r"""Look up the link_index with key ``tid``. If the link index is not
        built, this will throw a ``PackIndexError``.

        Args:
            tid (int): the tid of the entry being looked up.
            as_parent (bool): If `as_patent` is True, will look up
                :attr:`link_index["parent_index"] and return the tids of links
                whose parent is `tid`. Otherwise,  will look up
                :attr:`link_index["child_index"] and return the tids of links
                whose child is `tid`.
        """
        if not self._link_index_switch:
            raise PackIndexError("Link index for pack not build")

        if as_parent:
            return self._link_index["parent_index"][tid]
        else:
            return self._link_index["child_index"][tid]

    def group_index(self, tid: int) -> Set[int]:
        r"""Look up the group_index with key `tid`. If the index is not built,
        this will raise a ``PackIndexError``.
        """
        if not self.group_index_on:
            raise PackIndexError("Group index for pack not build")
        return self._group_index[tid]

    def update_link_index(self, links: List[LinkType]):
        r"""Update :attr:`link_index` with the provided links, the index from
        child and parent to links.

        :attr:`link_index` consists of two sub-indexes:
            - "child_index" is the index from child nodes to their corresponding
              links
            - "parent_index" is the index from parent nodes to their
              corresponding links.

        Args:
            links (list): a list of links to be added into the index.
        """
        if not self.link_index_on:
            raise PackIndexError("Link index has not been built.")

        for link in links:
            self._link_index["child_index"][link.get_child().index_key].add(
                link.index_key
            )
            self._link_index["parent_index"][link.get_parent().index_key].add(
                link.index_key
            )

    def update_group_index(self, groups: List[GroupType]):
        r"""Build or update :attr:`group_index`, the index from group members
        to groups.

        Args:
            groups (list): a list of groups to be added into the index.
        """
        logger.debug("Updating group index")

        if not self._group_index:
            raise PackIndexError("Group index has not been built.")

        for group in groups:
            for member in group.members:
                self._group_index[member].add(group.tid)

    def add_link_parent(self, parent: EntryType, link: LinkType):
        self._link_index["parent_index"][parent.index_key].add(link.tid)

    def add_link_child(self, child: EntryType, link: LinkType):
        self._link_index["child_index"][child.index_key].add(link.tid)

    def add_group_member(self, member: EntryType, group: GroupType):
        self._group_index[member.index_key].add(group.tid)

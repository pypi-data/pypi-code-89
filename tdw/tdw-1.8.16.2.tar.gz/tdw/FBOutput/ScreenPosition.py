# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class ScreenPosition(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsScreenPosition(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = ScreenPosition()
        x.Init(buf, n + offset)
        return x

    # ScreenPosition
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # ScreenPosition
    def AvatarId(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ScreenPosition
    def SensorName(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ScreenPosition
    def Id(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ScreenPosition
    def World(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ScreenPosition
    def Screen(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ScreenPositionStart(builder): builder.StartObject(5)
def ScreenPositionAddAvatarId(builder, avatarId): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(avatarId), 0)
def ScreenPositionAddSensorName(builder, sensorName): builder.PrependUOffsetTRelativeSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(sensorName), 0)
def ScreenPositionAddId(builder, id): builder.PrependInt32Slot(2, id, 0)
def ScreenPositionAddWorld(builder, world): builder.PrependStructSlot(3, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(world), 0)
def ScreenPositionAddScreen(builder, screen): builder.PrependStructSlot(4, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(screen), 0)
def ScreenPositionEnd(builder): return builder.EndObject()

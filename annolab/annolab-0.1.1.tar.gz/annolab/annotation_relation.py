from typing import Dict


class AnnotationRelation:

  @staticmethod
  def create_api_relation(dict: Dict):
    """
    Maps an sdk relation dict to an api annotation relation dict, for use in calls to the api.

    AnnotationRelation parameters:
      annotations: [Union[str, int], Union[str, int]]
      type:        str
      schema:      str
      value:       str
      reviewed     bool (Optional)
    """
    relation = {
      'predecessorId': str(dict['annotations'][0]),
      'successorId': str(dict['annotations'][1])
    }

    if ('type' in dict): relation['typeIdentifier'] = dict['client_id']
    if ('schema' in dict): relation['schemaIdentifier'] = dict['schema']
    if ('value' in dict): relation['value'] = dict['value']
    if ('reviewed' in dict): relation['isReviewed'] = dict['reviewed']

    return relation
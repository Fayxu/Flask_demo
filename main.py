import pytest
from unit.read_yaml import YamlUtil

if __name__ == '__main__':
    pytest.main(['-vs'])
    # YamlUtil('./extract.yaml').write_yaml({"sex": "male",
    #                                                     "name": "jack",
    #                                                     "age": 20
    #                                                     })
from enum import Enum


class QueryMode(str, Enum):
    default = "default"
    insensitive = "insensitive"


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"


class Test1ScalarFieldEnum(str, Enum):
    createdById = "createdById"
    id = "id"
    name = "name"


class Test2ScalarFieldEnum(str, Enum):
    createdById = "createdById"
    id = "id"
    name = "name"


class Test3ScalarFieldEnum(str, Enum):
    createdById = "createdById"
    id = "id"
    name = "name"
    test2Id = "test2Id"
    test5Id = "test5Id"


class Test4ScalarFieldEnum(str, Enum):
    createdById = "createdById"
    id = "id"
    name = "name"
    test1Id = "test1Id"
    test2Id = "test2Id"
    test3Id = "test3Id"
    test5Id = "test5Id"


class Test5ScalarFieldEnum(str, Enum):
    createdById = "createdById"
    id = "id"
    name = "name"


class UserScalarFieldEnum(str, Enum):
    id = "id"
    name = "name"

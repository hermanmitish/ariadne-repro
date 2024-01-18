from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import QueryMode, SortOrder


class NestedIntFilter(BaseModel):
    equals: Optional[int] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    in_: Optional[List[int]] = Field(alias="in", default=None)
    lt: Optional[int] = None
    lte: Optional[int] = None
    not_: Optional["NestedIntFilter"] = Field(alias="not", default=None)
    notIn: Optional[List[int]] = None


class NestedIntNullableFilter(BaseModel):
    equals: Optional[int] = None
    gt: Optional[int] = None
    gte: Optional[int] = None
    in_: Optional[List[int]] = Field(alias="in", default=None)
    isSet: Optional[bool] = None
    lt: Optional[int] = None
    lte: Optional[int] = None
    not_: Optional["NestedIntNullableFilter"] = Field(alias="not", default=None)
    notIn: Optional[List[int]] = None


class NestedStringFilter(BaseModel):
    contains: Optional[str] = None
    endsWith: Optional[str] = None
    equals: Optional[str] = None
    gt: Optional[str] = None
    gte: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    lt: Optional[str] = None
    lte: Optional[str] = None
    not_: Optional["NestedStringFilter"] = Field(alias="not", default=None)
    notIn: Optional[List[str]] = None
    startsWith: Optional[str] = None


class NestedStringNullableFilter(BaseModel):
    contains: Optional[str] = None
    endsWith: Optional[str] = None
    equals: Optional[str] = None
    gt: Optional[str] = None
    gte: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    isSet: Optional[bool] = None
    lt: Optional[str] = None
    lte: Optional[str] = None
    not_: Optional["NestedStringNullableFilter"] = Field(alias="not", default=None)
    notIn: Optional[List[str]] = None
    startsWith: Optional[str] = None


class NestedStringNullableWithAggregatesFilter(BaseModel):
    count: Optional["NestedIntNullableFilter"] = Field(alias="_count", default=None)
    max: Optional["NestedStringNullableFilter"] = Field(alias="_max", default=None)
    min: Optional["NestedStringNullableFilter"] = Field(alias="_min", default=None)
    contains: Optional[str] = None
    endsWith: Optional[str] = None
    equals: Optional[str] = None
    gt: Optional[str] = None
    gte: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    isSet: Optional[bool] = None
    lt: Optional[str] = None
    lte: Optional[str] = None
    not_: Optional["NestedStringNullableWithAggregatesFilter"] = Field(
        alias="not", default=None
    )
    notIn: Optional[List[str]] = None
    startsWith: Optional[str] = None


class NestedStringWithAggregatesFilter(BaseModel):
    count: Optional["NestedIntFilter"] = Field(alias="_count", default=None)
    max: Optional["NestedStringFilter"] = Field(alias="_max", default=None)
    min: Optional["NestedStringFilter"] = Field(alias="_min", default=None)
    contains: Optional[str] = None
    endsWith: Optional[str] = None
    equals: Optional[str] = None
    gt: Optional[str] = None
    gte: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    lt: Optional[str] = None
    lte: Optional[str] = None
    not_: Optional["NestedStringWithAggregatesFilter"] = Field(
        alias="not", default=None
    )
    notIn: Optional[List[str]] = None
    startsWith: Optional[str] = None


class NullableStringFieldUpdateOperationsInput(BaseModel):
    set: Optional[str] = None
    unset: Optional[bool] = None


class StringFieldUpdateOperationsInput(BaseModel):
    set: Optional[str] = None


class StringFilter(BaseModel):
    contains: Optional[str] = None
    endsWith: Optional[str] = None
    equals: Optional[str] = None
    gt: Optional[str] = None
    gte: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    lt: Optional[str] = None
    lte: Optional[str] = None
    mode: Optional[QueryMode] = None
    not_: Optional["NestedStringFilter"] = Field(alias="not", default=None)
    notIn: Optional[List[str]] = None
    startsWith: Optional[str] = None


class StringNullableFilter(BaseModel):
    contains: Optional[str] = None
    endsWith: Optional[str] = None
    equals: Optional[str] = None
    gt: Optional[str] = None
    gte: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    isSet: Optional[bool] = None
    lt: Optional[str] = None
    lte: Optional[str] = None
    mode: Optional[QueryMode] = None
    not_: Optional["NestedStringNullableFilter"] = Field(alias="not", default=None)
    notIn: Optional[List[str]] = None
    startsWith: Optional[str] = None


class StringNullableWithAggregatesFilter(BaseModel):
    count: Optional["NestedIntNullableFilter"] = Field(alias="_count", default=None)
    max: Optional["NestedStringNullableFilter"] = Field(alias="_max", default=None)
    min: Optional["NestedStringNullableFilter"] = Field(alias="_min", default=None)
    contains: Optional[str] = None
    endsWith: Optional[str] = None
    equals: Optional[str] = None
    gt: Optional[str] = None
    gte: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    isSet: Optional[bool] = None
    lt: Optional[str] = None
    lte: Optional[str] = None
    mode: Optional[QueryMode] = None
    not_: Optional["NestedStringNullableWithAggregatesFilter"] = Field(
        alias="not", default=None
    )
    notIn: Optional[List[str]] = None
    startsWith: Optional[str] = None


class StringWithAggregatesFilter(BaseModel):
    count: Optional["NestedIntFilter"] = Field(alias="_count", default=None)
    max: Optional["NestedStringFilter"] = Field(alias="_max", default=None)
    min: Optional["NestedStringFilter"] = Field(alias="_min", default=None)
    contains: Optional[str] = None
    endsWith: Optional[str] = None
    equals: Optional[str] = None
    gt: Optional[str] = None
    gte: Optional[str] = None
    in_: Optional[List[str]] = Field(alias="in", default=None)
    lt: Optional[str] = None
    lte: Optional[str] = None
    mode: Optional[QueryMode] = None
    not_: Optional["NestedStringWithAggregatesFilter"] = Field(
        alias="not", default=None
    )
    notIn: Optional[List[str]] = None
    startsWith: Optional[str] = None


class Test1CountOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test1CreateInput(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest1Input"] = None
    id: Optional[str] = None
    name: str
    test4: Optional["Test4CreateNestedManyWithoutTest1Input"] = None


class Test1CreateManyCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str


class Test1CreateManyCreatedByInputEnvelope(BaseModel):
    data: List["Test1CreateManyCreatedByInput"]


class Test1CreateManyInput(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str


class Test1CreateNestedManyWithoutCreatedByInput(BaseModel):
    connect: Optional[List["Test1WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test1CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test1CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test1CreateManyCreatedByInputEnvelope"] = None


class Test1CreateNestedOneWithoutTest4Input(BaseModel):
    connect: Optional["Test1WhereUniqueInput"] = None
    connectOrCreate: Optional["Test1CreateOrConnectWithoutTest4Input"] = None
    create: Optional["Test1CreateWithoutTest4Input"] = None


class Test1CreateOrConnectWithoutCreatedByInput(BaseModel):
    create: "Test1CreateWithoutCreatedByInput"
    where: "Test1WhereUniqueInput"


class Test1CreateOrConnectWithoutTest4Input(BaseModel):
    create: "Test1CreateWithoutTest4Input"
    where: "Test1WhereUniqueInput"


class Test1CreateWithoutCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str
    test4: Optional["Test4CreateNestedManyWithoutTest1Input"] = None


class Test1CreateWithoutTest4Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest1Input"] = None
    id: Optional[str] = None
    name: str


class Test1ListRelationFilter(BaseModel):
    every: Optional["Test1WhereInput"] = None
    none: Optional["Test1WhereInput"] = None
    some: Optional["Test1WhereInput"] = None


class Test1MaxOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test1MinOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test1NullableRelationFilter(BaseModel):
    is_: Optional["Test1WhereInput"] = Field(alias="is", default=None)
    isNot: Optional["Test1WhereInput"] = None


class Test1OrderByRelationAggregateInput(BaseModel):
    count: Optional[SortOrder] = Field(alias="_count", default=None)


class Test1OrderByWithAggregationInput(BaseModel):
    count: Optional["Test1CountOrderByAggregateInput"] = Field(
        alias="_count", default=None
    )
    max: Optional["Test1MaxOrderByAggregateInput"] = Field(alias="_max", default=None)
    min: Optional["Test1MinOrderByAggregateInput"] = Field(alias="_min", default=None)
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test1OrderByWithRelationInput(BaseModel):
    createdBy: Optional["UserOrderByWithRelationInput"] = None
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test4: Optional["Test4OrderByRelationAggregateInput"] = None


class Test1ScalarWhereInput(BaseModel):
    AND: Optional[List["Test1ScalarWhereInput"]] = None
    NOT: Optional[List["Test1ScalarWhereInput"]] = None
    OR: Optional[List["Test1ScalarWhereInput"]] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None


class Test1ScalarWhereWithAggregatesInput(BaseModel):
    AND: Optional[List["Test1ScalarWhereWithAggregatesInput"]] = None
    NOT: Optional[List["Test1ScalarWhereWithAggregatesInput"]] = None
    OR: Optional[List["Test1ScalarWhereWithAggregatesInput"]] = None
    createdById: Optional["StringNullableWithAggregatesFilter"] = None
    id: Optional["StringWithAggregatesFilter"] = None
    name: Optional["StringWithAggregatesFilter"] = None


class Test1UpdateInput(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest1NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest1NestedInput"] = None


class Test1UpdateManyMutationInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None


class Test1UpdateManyWithWhereWithoutCreatedByInput(BaseModel):
    data: "Test1UpdateManyMutationInput"
    where: "Test1ScalarWhereInput"


class Test1UpdateManyWithoutCreatedByNestedInput(BaseModel):
    connect: Optional[List["Test1WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test1CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test1CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test1CreateManyCreatedByInputEnvelope"] = None
    delete: Optional[List["Test1WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test1ScalarWhereInput"]] = None
    disconnect: Optional[List["Test1WhereUniqueInput"]] = None
    set: Optional[List["Test1WhereUniqueInput"]] = None
    update: Optional[List["Test1UpdateWithWhereUniqueWithoutCreatedByInput"]] = None
    updateMany: Optional[List["Test1UpdateManyWithWhereWithoutCreatedByInput"]] = None
    upsert: Optional[List["Test1UpsertWithWhereUniqueWithoutCreatedByInput"]] = None


class Test1UpdateOneWithoutTest4NestedInput(BaseModel):
    connect: Optional["Test1WhereUniqueInput"] = None
    connectOrCreate: Optional["Test1CreateOrConnectWithoutTest4Input"] = None
    create: Optional["Test1CreateWithoutTest4Input"] = None
    delete: Optional["Test1WhereInput"] = None
    disconnect: Optional[bool] = None
    update: Optional["Test1UpdateToOneWithWhereWithoutTest4Input"] = None
    upsert: Optional["Test1UpsertWithoutTest4Input"] = None


class Test1UpdateToOneWithWhereWithoutTest4Input(BaseModel):
    data: "Test1UpdateWithoutTest4Input"
    where: Optional["Test1WhereInput"] = None


class Test1UpdateWithWhereUniqueWithoutCreatedByInput(BaseModel):
    data: "Test1UpdateWithoutCreatedByInput"
    where: "Test1WhereUniqueInput"


class Test1UpdateWithoutCreatedByInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest1NestedInput"] = None


class Test1UpdateWithoutTest4Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest1NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None


class Test1UpsertWithWhereUniqueWithoutCreatedByInput(BaseModel):
    create: "Test1CreateWithoutCreatedByInput"
    update: "Test1UpdateWithoutCreatedByInput"
    where: "Test1WhereUniqueInput"


class Test1UpsertWithoutTest4Input(BaseModel):
    create: "Test1CreateWithoutTest4Input"
    update: "Test1UpdateWithoutTest4Input"
    where: Optional["Test1WhereInput"] = None


class Test1WhereInput(BaseModel):
    AND: Optional[List["Test1WhereInput"]] = None
    NOT: Optional[List["Test1WhereInput"]] = None
    OR: Optional[List["Test1WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None


class Test1WhereUniqueInput(BaseModel):
    AND: Optional[List["Test1WhereInput"]] = None
    NOT: Optional[List["Test1WhereInput"]] = None
    OR: Optional[List["Test1WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional[str] = None
    name: Optional["StringFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None


class Test2CountOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test2CreateInput(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest2Input"] = None
    id: Optional[str] = None
    name: str
    test3: Optional["Test3CreateNestedManyWithoutTest2Input"] = None
    test4: Optional["Test4CreateNestedManyWithoutTest2Input"] = None


class Test2CreateManyCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str


class Test2CreateManyCreatedByInputEnvelope(BaseModel):
    data: List["Test2CreateManyCreatedByInput"]


class Test2CreateManyInput(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str


class Test2CreateNestedManyWithoutCreatedByInput(BaseModel):
    connect: Optional[List["Test2WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test2CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test2CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test2CreateManyCreatedByInputEnvelope"] = None


class Test2CreateNestedOneWithoutTest3Input(BaseModel):
    connect: Optional["Test2WhereUniqueInput"] = None
    connectOrCreate: Optional["Test2CreateOrConnectWithoutTest3Input"] = None
    create: Optional["Test2CreateWithoutTest3Input"] = None


class Test2CreateNestedOneWithoutTest4Input(BaseModel):
    connect: Optional["Test2WhereUniqueInput"] = None
    connectOrCreate: Optional["Test2CreateOrConnectWithoutTest4Input"] = None
    create: Optional["Test2CreateWithoutTest4Input"] = None


class Test2CreateOrConnectWithoutCreatedByInput(BaseModel):
    create: "Test2CreateWithoutCreatedByInput"
    where: "Test2WhereUniqueInput"


class Test2CreateOrConnectWithoutTest3Input(BaseModel):
    create: "Test2CreateWithoutTest3Input"
    where: "Test2WhereUniqueInput"


class Test2CreateOrConnectWithoutTest4Input(BaseModel):
    create: "Test2CreateWithoutTest4Input"
    where: "Test2WhereUniqueInput"


class Test2CreateWithoutCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str
    test3: Optional["Test3CreateNestedManyWithoutTest2Input"] = None
    test4: Optional["Test4CreateNestedManyWithoutTest2Input"] = None


class Test2CreateWithoutTest3Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest2Input"] = None
    id: Optional[str] = None
    name: str
    test4: Optional["Test4CreateNestedManyWithoutTest2Input"] = None


class Test2CreateWithoutTest4Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest2Input"] = None
    id: Optional[str] = None
    name: str
    test3: Optional["Test3CreateNestedManyWithoutTest2Input"] = None


class Test2ListRelationFilter(BaseModel):
    every: Optional["Test2WhereInput"] = None
    none: Optional["Test2WhereInput"] = None
    some: Optional["Test2WhereInput"] = None


class Test2MaxOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test2MinOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test2NullableRelationFilter(BaseModel):
    is_: Optional["Test2WhereInput"] = Field(alias="is", default=None)
    isNot: Optional["Test2WhereInput"] = None


class Test2OrderByRelationAggregateInput(BaseModel):
    count: Optional[SortOrder] = Field(alias="_count", default=None)


class Test2OrderByWithAggregationInput(BaseModel):
    count: Optional["Test2CountOrderByAggregateInput"] = Field(
        alias="_count", default=None
    )
    max: Optional["Test2MaxOrderByAggregateInput"] = Field(alias="_max", default=None)
    min: Optional["Test2MinOrderByAggregateInput"] = Field(alias="_min", default=None)
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test2OrderByWithRelationInput(BaseModel):
    createdBy: Optional["UserOrderByWithRelationInput"] = None
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test3: Optional["Test3OrderByRelationAggregateInput"] = None
    test4: Optional["Test4OrderByRelationAggregateInput"] = None


class Test2RelationFilter(BaseModel):
    is_: Optional["Test2WhereInput"] = Field(alias="is", default=None)
    isNot: Optional["Test2WhereInput"] = None


class Test2ScalarWhereInput(BaseModel):
    AND: Optional[List["Test2ScalarWhereInput"]] = None
    NOT: Optional[List["Test2ScalarWhereInput"]] = None
    OR: Optional[List["Test2ScalarWhereInput"]] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None


class Test2ScalarWhereWithAggregatesInput(BaseModel):
    AND: Optional[List["Test2ScalarWhereWithAggregatesInput"]] = None
    NOT: Optional[List["Test2ScalarWhereWithAggregatesInput"]] = None
    OR: Optional[List["Test2ScalarWhereWithAggregatesInput"]] = None
    createdById: Optional["StringNullableWithAggregatesFilter"] = None
    id: Optional["StringWithAggregatesFilter"] = None
    name: Optional["StringWithAggregatesFilter"] = None


class Test2UpdateInput(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest2NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test3: Optional["Test3UpdateManyWithoutTest2NestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest2NestedInput"] = None


class Test2UpdateManyMutationInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None


class Test2UpdateManyWithWhereWithoutCreatedByInput(BaseModel):
    data: "Test2UpdateManyMutationInput"
    where: "Test2ScalarWhereInput"


class Test2UpdateManyWithoutCreatedByNestedInput(BaseModel):
    connect: Optional[List["Test2WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test2CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test2CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test2CreateManyCreatedByInputEnvelope"] = None
    delete: Optional[List["Test2WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test2ScalarWhereInput"]] = None
    disconnect: Optional[List["Test2WhereUniqueInput"]] = None
    set: Optional[List["Test2WhereUniqueInput"]] = None
    update: Optional[List["Test2UpdateWithWhereUniqueWithoutCreatedByInput"]] = None
    updateMany: Optional[List["Test2UpdateManyWithWhereWithoutCreatedByInput"]] = None
    upsert: Optional[List["Test2UpsertWithWhereUniqueWithoutCreatedByInput"]] = None


class Test2UpdateOneRequiredWithoutTest3NestedInput(BaseModel):
    connect: Optional["Test2WhereUniqueInput"] = None
    connectOrCreate: Optional["Test2CreateOrConnectWithoutTest3Input"] = None
    create: Optional["Test2CreateWithoutTest3Input"] = None
    update: Optional["Test2UpdateToOneWithWhereWithoutTest3Input"] = None
    upsert: Optional["Test2UpsertWithoutTest3Input"] = None


class Test2UpdateOneWithoutTest4NestedInput(BaseModel):
    connect: Optional["Test2WhereUniqueInput"] = None
    connectOrCreate: Optional["Test2CreateOrConnectWithoutTest4Input"] = None
    create: Optional["Test2CreateWithoutTest4Input"] = None
    delete: Optional["Test2WhereInput"] = None
    disconnect: Optional[bool] = None
    update: Optional["Test2UpdateToOneWithWhereWithoutTest4Input"] = None
    upsert: Optional["Test2UpsertWithoutTest4Input"] = None


class Test2UpdateToOneWithWhereWithoutTest3Input(BaseModel):
    data: "Test2UpdateWithoutTest3Input"
    where: Optional["Test2WhereInput"] = None


class Test2UpdateToOneWithWhereWithoutTest4Input(BaseModel):
    data: "Test2UpdateWithoutTest4Input"
    where: Optional["Test2WhereInput"] = None


class Test2UpdateWithWhereUniqueWithoutCreatedByInput(BaseModel):
    data: "Test2UpdateWithoutCreatedByInput"
    where: "Test2WhereUniqueInput"


class Test2UpdateWithoutCreatedByInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test3: Optional["Test3UpdateManyWithoutTest2NestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest2NestedInput"] = None


class Test2UpdateWithoutTest3Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest2NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest2NestedInput"] = None


class Test2UpdateWithoutTest4Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest2NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test3: Optional["Test3UpdateManyWithoutTest2NestedInput"] = None


class Test2UpsertWithWhereUniqueWithoutCreatedByInput(BaseModel):
    create: "Test2CreateWithoutCreatedByInput"
    update: "Test2UpdateWithoutCreatedByInput"
    where: "Test2WhereUniqueInput"


class Test2UpsertWithoutTest3Input(BaseModel):
    create: "Test2CreateWithoutTest3Input"
    update: "Test2UpdateWithoutTest3Input"
    where: Optional["Test2WhereInput"] = None


class Test2UpsertWithoutTest4Input(BaseModel):
    create: "Test2CreateWithoutTest4Input"
    update: "Test2UpdateWithoutTest4Input"
    where: Optional["Test2WhereInput"] = None


class Test2WhereInput(BaseModel):
    AND: Optional[List["Test2WhereInput"]] = None
    NOT: Optional[List["Test2WhereInput"]] = None
    OR: Optional[List["Test2WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None
    test3: Optional["Test3ListRelationFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None


class Test2WhereUniqueInput(BaseModel):
    AND: Optional[List["Test2WhereInput"]] = None
    NOT: Optional[List["Test2WhereInput"]] = None
    OR: Optional[List["Test2WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional[str] = None
    name: Optional[str] = None
    test3: Optional["Test3ListRelationFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None


class Test3CountOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test2Id: Optional[SortOrder] = None
    test5Id: Optional[SortOrder] = None


class Test3CreateInput(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest3Input"] = None
    id: Optional[str] = None
    name: str
    test2: "Test2CreateNestedOneWithoutTest3Input"
    test4: Optional["Test4CreateNestedManyWithoutTest3Input"] = None
    test5: "Test5CreateNestedOneWithoutTest3Input"


class Test3CreateManyCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str
    test2Id: str
    test5Id: str


class Test3CreateManyCreatedByInputEnvelope(BaseModel):
    data: List["Test3CreateManyCreatedByInput"]


class Test3CreateManyInput(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str
    test2Id: str
    test5Id: str


class Test3CreateManyTest2Input(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str
    test5Id: str


class Test3CreateManyTest2InputEnvelope(BaseModel):
    data: List["Test3CreateManyTest2Input"]


class Test3CreateManyTest5Input(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str
    test2Id: str


class Test3CreateManyTest5InputEnvelope(BaseModel):
    data: List["Test3CreateManyTest5Input"]


class Test3CreateNestedManyWithoutCreatedByInput(BaseModel):
    connect: Optional[List["Test3WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test3CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test3CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test3CreateManyCreatedByInputEnvelope"] = None


class Test3CreateNestedManyWithoutTest2Input(BaseModel):
    connect: Optional[List["Test3WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test3CreateOrConnectWithoutTest2Input"]] = None
    create: Optional[List["Test3CreateWithoutTest2Input"]] = None
    createMany: Optional["Test3CreateManyTest2InputEnvelope"] = None


class Test3CreateNestedManyWithoutTest5Input(BaseModel):
    connect: Optional[List["Test3WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test3CreateOrConnectWithoutTest5Input"]] = None
    create: Optional[List["Test3CreateWithoutTest5Input"]] = None
    createMany: Optional["Test3CreateManyTest5InputEnvelope"] = None


class Test3CreateNestedOneWithoutTest4Input(BaseModel):
    connect: Optional["Test3WhereUniqueInput"] = None
    connectOrCreate: Optional["Test3CreateOrConnectWithoutTest4Input"] = None
    create: Optional["Test3CreateWithoutTest4Input"] = None


class Test3CreateOrConnectWithoutCreatedByInput(BaseModel):
    create: "Test3CreateWithoutCreatedByInput"
    where: "Test3WhereUniqueInput"


class Test3CreateOrConnectWithoutTest2Input(BaseModel):
    create: "Test3CreateWithoutTest2Input"
    where: "Test3WhereUniqueInput"


class Test3CreateOrConnectWithoutTest4Input(BaseModel):
    create: "Test3CreateWithoutTest4Input"
    where: "Test3WhereUniqueInput"


class Test3CreateOrConnectWithoutTest5Input(BaseModel):
    create: "Test3CreateWithoutTest5Input"
    where: "Test3WhereUniqueInput"


class Test3CreateWithoutCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str
    test2: "Test2CreateNestedOneWithoutTest3Input"
    test4: Optional["Test4CreateNestedManyWithoutTest3Input"] = None
    test5: "Test5CreateNestedOneWithoutTest3Input"


class Test3CreateWithoutTest2Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest3Input"] = None
    id: Optional[str] = None
    name: str
    test4: Optional["Test4CreateNestedManyWithoutTest3Input"] = None
    test5: "Test5CreateNestedOneWithoutTest3Input"


class Test3CreateWithoutTest4Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest3Input"] = None
    id: Optional[str] = None
    name: str
    test2: "Test2CreateNestedOneWithoutTest3Input"
    test5: "Test5CreateNestedOneWithoutTest3Input"


class Test3CreateWithoutTest5Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest3Input"] = None
    id: Optional[str] = None
    name: str
    test2: "Test2CreateNestedOneWithoutTest3Input"
    test4: Optional["Test4CreateNestedManyWithoutTest3Input"] = None


class Test3ListRelationFilter(BaseModel):
    every: Optional["Test3WhereInput"] = None
    none: Optional["Test3WhereInput"] = None
    some: Optional["Test3WhereInput"] = None


class Test3MaxOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test2Id: Optional[SortOrder] = None
    test5Id: Optional[SortOrder] = None


class Test3MinOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test2Id: Optional[SortOrder] = None
    test5Id: Optional[SortOrder] = None


class Test3OrderByRelationAggregateInput(BaseModel):
    count: Optional[SortOrder] = Field(alias="_count", default=None)


class Test3OrderByWithAggregationInput(BaseModel):
    count: Optional["Test3CountOrderByAggregateInput"] = Field(
        alias="_count", default=None
    )
    max: Optional["Test3MaxOrderByAggregateInput"] = Field(alias="_max", default=None)
    min: Optional["Test3MinOrderByAggregateInput"] = Field(alias="_min", default=None)
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test2Id: Optional[SortOrder] = None
    test5Id: Optional[SortOrder] = None


class Test3OrderByWithRelationInput(BaseModel):
    createdBy: Optional["UserOrderByWithRelationInput"] = None
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test2: Optional["Test2OrderByWithRelationInput"] = None
    test2Id: Optional[SortOrder] = None
    test4: Optional["Test4OrderByRelationAggregateInput"] = None
    test5: Optional["Test5OrderByWithRelationInput"] = None
    test5Id: Optional[SortOrder] = None


class Test3RelationFilter(BaseModel):
    is_: Optional["Test3WhereInput"] = Field(alias="is", default=None)
    isNot: Optional["Test3WhereInput"] = None


class Test3ScalarWhereInput(BaseModel):
    AND: Optional[List["Test3ScalarWhereInput"]] = None
    NOT: Optional[List["Test3ScalarWhereInput"]] = None
    OR: Optional[List["Test3ScalarWhereInput"]] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None
    test2Id: Optional["StringFilter"] = None
    test5Id: Optional["StringFilter"] = None


class Test3ScalarWhereWithAggregatesInput(BaseModel):
    AND: Optional[List["Test3ScalarWhereWithAggregatesInput"]] = None
    NOT: Optional[List["Test3ScalarWhereWithAggregatesInput"]] = None
    OR: Optional[List["Test3ScalarWhereWithAggregatesInput"]] = None
    createdById: Optional["StringNullableWithAggregatesFilter"] = None
    id: Optional["StringWithAggregatesFilter"] = None
    name: Optional["StringWithAggregatesFilter"] = None
    test2Id: Optional["StringWithAggregatesFilter"] = None
    test5Id: Optional["StringWithAggregatesFilter"] = None


class Test3UpdateInput(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest3NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test2: Optional["Test2UpdateOneRequiredWithoutTest3NestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest3NestedInput"] = None
    test5: Optional["Test5UpdateOneRequiredWithoutTest3NestedInput"] = None


class Test3UpdateManyMutationInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None


class Test3UpdateManyWithWhereWithoutCreatedByInput(BaseModel):
    data: "Test3UpdateManyMutationInput"
    where: "Test3ScalarWhereInput"


class Test3UpdateManyWithWhereWithoutTest2Input(BaseModel):
    data: "Test3UpdateManyMutationInput"
    where: "Test3ScalarWhereInput"


class Test3UpdateManyWithWhereWithoutTest5Input(BaseModel):
    data: "Test3UpdateManyMutationInput"
    where: "Test3ScalarWhereInput"


class Test3UpdateManyWithoutCreatedByNestedInput(BaseModel):
    connect: Optional[List["Test3WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test3CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test3CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test3CreateManyCreatedByInputEnvelope"] = None
    delete: Optional[List["Test3WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test3ScalarWhereInput"]] = None
    disconnect: Optional[List["Test3WhereUniqueInput"]] = None
    set: Optional[List["Test3WhereUniqueInput"]] = None
    update: Optional[List["Test3UpdateWithWhereUniqueWithoutCreatedByInput"]] = None
    updateMany: Optional[List["Test3UpdateManyWithWhereWithoutCreatedByInput"]] = None
    upsert: Optional[List["Test3UpsertWithWhereUniqueWithoutCreatedByInput"]] = None


class Test3UpdateManyWithoutTest2NestedInput(BaseModel):
    connect: Optional[List["Test3WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test3CreateOrConnectWithoutTest2Input"]] = None
    create: Optional[List["Test3CreateWithoutTest2Input"]] = None
    createMany: Optional["Test3CreateManyTest2InputEnvelope"] = None
    delete: Optional[List["Test3WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test3ScalarWhereInput"]] = None
    disconnect: Optional[List["Test3WhereUniqueInput"]] = None
    set: Optional[List["Test3WhereUniqueInput"]] = None
    update: Optional[List["Test3UpdateWithWhereUniqueWithoutTest2Input"]] = None
    updateMany: Optional[List["Test3UpdateManyWithWhereWithoutTest2Input"]] = None
    upsert: Optional[List["Test3UpsertWithWhereUniqueWithoutTest2Input"]] = None


class Test3UpdateManyWithoutTest5NestedInput(BaseModel):
    connect: Optional[List["Test3WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test3CreateOrConnectWithoutTest5Input"]] = None
    create: Optional[List["Test3CreateWithoutTest5Input"]] = None
    createMany: Optional["Test3CreateManyTest5InputEnvelope"] = None
    delete: Optional[List["Test3WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test3ScalarWhereInput"]] = None
    disconnect: Optional[List["Test3WhereUniqueInput"]] = None
    set: Optional[List["Test3WhereUniqueInput"]] = None
    update: Optional[List["Test3UpdateWithWhereUniqueWithoutTest5Input"]] = None
    updateMany: Optional[List["Test3UpdateManyWithWhereWithoutTest5Input"]] = None
    upsert: Optional[List["Test3UpsertWithWhereUniqueWithoutTest5Input"]] = None


class Test3UpdateOneRequiredWithoutTest4NestedInput(BaseModel):
    connect: Optional["Test3WhereUniqueInput"] = None
    connectOrCreate: Optional["Test3CreateOrConnectWithoutTest4Input"] = None
    create: Optional["Test3CreateWithoutTest4Input"] = None
    update: Optional["Test3UpdateToOneWithWhereWithoutTest4Input"] = None
    upsert: Optional["Test3UpsertWithoutTest4Input"] = None


class Test3UpdateToOneWithWhereWithoutTest4Input(BaseModel):
    data: "Test3UpdateWithoutTest4Input"
    where: Optional["Test3WhereInput"] = None


class Test3UpdateWithWhereUniqueWithoutCreatedByInput(BaseModel):
    data: "Test3UpdateWithoutCreatedByInput"
    where: "Test3WhereUniqueInput"


class Test3UpdateWithWhereUniqueWithoutTest2Input(BaseModel):
    data: "Test3UpdateWithoutTest2Input"
    where: "Test3WhereUniqueInput"


class Test3UpdateWithWhereUniqueWithoutTest5Input(BaseModel):
    data: "Test3UpdateWithoutTest5Input"
    where: "Test3WhereUniqueInput"


class Test3UpdateWithoutCreatedByInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test2: Optional["Test2UpdateOneRequiredWithoutTest3NestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest3NestedInput"] = None
    test5: Optional["Test5UpdateOneRequiredWithoutTest3NestedInput"] = None


class Test3UpdateWithoutTest2Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest3NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest3NestedInput"] = None
    test5: Optional["Test5UpdateOneRequiredWithoutTest3NestedInput"] = None


class Test3UpdateWithoutTest4Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest3NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test2: Optional["Test2UpdateOneRequiredWithoutTest3NestedInput"] = None
    test5: Optional["Test5UpdateOneRequiredWithoutTest3NestedInput"] = None


class Test3UpdateWithoutTest5Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest3NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test2: Optional["Test2UpdateOneRequiredWithoutTest3NestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest3NestedInput"] = None


class Test3UpsertWithWhereUniqueWithoutCreatedByInput(BaseModel):
    create: "Test3CreateWithoutCreatedByInput"
    update: "Test3UpdateWithoutCreatedByInput"
    where: "Test3WhereUniqueInput"


class Test3UpsertWithWhereUniqueWithoutTest2Input(BaseModel):
    create: "Test3CreateWithoutTest2Input"
    update: "Test3UpdateWithoutTest2Input"
    where: "Test3WhereUniqueInput"


class Test3UpsertWithWhereUniqueWithoutTest5Input(BaseModel):
    create: "Test3CreateWithoutTest5Input"
    update: "Test3UpdateWithoutTest5Input"
    where: "Test3WhereUniqueInput"


class Test3UpsertWithoutTest4Input(BaseModel):
    create: "Test3CreateWithoutTest4Input"
    update: "Test3UpdateWithoutTest4Input"
    where: Optional["Test3WhereInput"] = None


class Test3WhereInput(BaseModel):
    AND: Optional[List["Test3WhereInput"]] = None
    NOT: Optional[List["Test3WhereInput"]] = None
    OR: Optional[List["Test3WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None
    test2: Optional["Test2RelationFilter"] = None
    test2Id: Optional["StringFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None
    test5: Optional["Test5RelationFilter"] = None
    test5Id: Optional["StringFilter"] = None


class Test3WhereUniqueInput(BaseModel):
    AND: Optional[List["Test3WhereInput"]] = None
    NOT: Optional[List["Test3WhereInput"]] = None
    OR: Optional[List["Test3WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional[str] = None
    name: Optional["StringFilter"] = None
    test2: Optional["Test2RelationFilter"] = None
    test2Id: Optional["StringFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None
    test5: Optional["Test5RelationFilter"] = None
    test5Id: Optional["StringFilter"] = None


class Test4CountOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test1Id: Optional[SortOrder] = None
    test2Id: Optional[SortOrder] = None
    test3Id: Optional[SortOrder] = None
    test5Id: Optional[SortOrder] = None


class Test4CreateInput(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest4Input"] = None
    id: Optional[str] = None
    name: str
    test1: Optional["Test1CreateNestedOneWithoutTest4Input"] = None
    test2: Optional["Test2CreateNestedOneWithoutTest4Input"] = None
    test3: "Test3CreateNestedOneWithoutTest4Input"
    test5: Optional["Test5CreateNestedOneWithoutTest4Input"] = None


class Test4CreateManyCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str
    test1Id: Optional[str] = None
    test2Id: str
    test3Id: str
    test5Id: Optional[str] = None


class Test4CreateManyCreatedByInputEnvelope(BaseModel):
    data: List["Test4CreateManyCreatedByInput"]


class Test4CreateManyInput(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str
    test1Id: Optional[str] = None
    test2Id: str
    test3Id: str
    test5Id: Optional[str] = None


class Test4CreateManyTest1Input(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str
    test2Id: str
    test3Id: str
    test5Id: Optional[str] = None


class Test4CreateManyTest1InputEnvelope(BaseModel):
    data: List["Test4CreateManyTest1Input"]


class Test4CreateManyTest2Input(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str
    test1Id: Optional[str] = None
    test3Id: str
    test5Id: Optional[str] = None


class Test4CreateManyTest2InputEnvelope(BaseModel):
    data: List["Test4CreateManyTest2Input"]


class Test4CreateManyTest3Input(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str
    test1Id: Optional[str] = None
    test2Id: str
    test5Id: Optional[str] = None


class Test4CreateManyTest3InputEnvelope(BaseModel):
    data: List["Test4CreateManyTest3Input"]


class Test4CreateManyTest5Input(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str
    test1Id: Optional[str] = None
    test2Id: str
    test3Id: str


class Test4CreateManyTest5InputEnvelope(BaseModel):
    data: List["Test4CreateManyTest5Input"]


class Test4CreateNestedManyWithoutCreatedByInput(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test4CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test4CreateManyCreatedByInputEnvelope"] = None


class Test4CreateNestedManyWithoutTest1Input(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutTest1Input"]] = None
    create: Optional[List["Test4CreateWithoutTest1Input"]] = None
    createMany: Optional["Test4CreateManyTest1InputEnvelope"] = None


class Test4CreateNestedManyWithoutTest2Input(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutTest2Input"]] = None
    create: Optional[List["Test4CreateWithoutTest2Input"]] = None
    createMany: Optional["Test4CreateManyTest2InputEnvelope"] = None


class Test4CreateNestedManyWithoutTest3Input(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutTest3Input"]] = None
    create: Optional[List["Test4CreateWithoutTest3Input"]] = None
    createMany: Optional["Test4CreateManyTest3InputEnvelope"] = None


class Test4CreateNestedManyWithoutTest5Input(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutTest5Input"]] = None
    create: Optional[List["Test4CreateWithoutTest5Input"]] = None
    createMany: Optional["Test4CreateManyTest5InputEnvelope"] = None


class Test4CreateOrConnectWithoutCreatedByInput(BaseModel):
    create: "Test4CreateWithoutCreatedByInput"
    where: "Test4WhereUniqueInput"


class Test4CreateOrConnectWithoutTest1Input(BaseModel):
    create: "Test4CreateWithoutTest1Input"
    where: "Test4WhereUniqueInput"


class Test4CreateOrConnectWithoutTest2Input(BaseModel):
    create: "Test4CreateWithoutTest2Input"
    where: "Test4WhereUniqueInput"


class Test4CreateOrConnectWithoutTest3Input(BaseModel):
    create: "Test4CreateWithoutTest3Input"
    where: "Test4WhereUniqueInput"


class Test4CreateOrConnectWithoutTest5Input(BaseModel):
    create: "Test4CreateWithoutTest5Input"
    where: "Test4WhereUniqueInput"


class Test4CreateWithoutCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str
    test1: Optional["Test1CreateNestedOneWithoutTest4Input"] = None
    test2: Optional["Test2CreateNestedOneWithoutTest4Input"] = None
    test3: "Test3CreateNestedOneWithoutTest4Input"
    test5: Optional["Test5CreateNestedOneWithoutTest4Input"] = None


class Test4CreateWithoutTest1Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest4Input"] = None
    id: Optional[str] = None
    name: str
    test2: Optional["Test2CreateNestedOneWithoutTest4Input"] = None
    test3: "Test3CreateNestedOneWithoutTest4Input"
    test5: Optional["Test5CreateNestedOneWithoutTest4Input"] = None


class Test4CreateWithoutTest2Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest4Input"] = None
    id: Optional[str] = None
    name: str
    test1: Optional["Test1CreateNestedOneWithoutTest4Input"] = None
    test3: "Test3CreateNestedOneWithoutTest4Input"
    test5: Optional["Test5CreateNestedOneWithoutTest4Input"] = None


class Test4CreateWithoutTest3Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest4Input"] = None
    id: Optional[str] = None
    name: str
    test1: Optional["Test1CreateNestedOneWithoutTest4Input"] = None
    test2: Optional["Test2CreateNestedOneWithoutTest4Input"] = None
    test5: Optional["Test5CreateNestedOneWithoutTest4Input"] = None


class Test4CreateWithoutTest5Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest4Input"] = None
    id: Optional[str] = None
    name: str
    test1: Optional["Test1CreateNestedOneWithoutTest4Input"] = None
    test2: Optional["Test2CreateNestedOneWithoutTest4Input"] = None
    test3: "Test3CreateNestedOneWithoutTest4Input"


class Test4ListRelationFilter(BaseModel):
    every: Optional["Test4WhereInput"] = None
    none: Optional["Test4WhereInput"] = None
    some: Optional["Test4WhereInput"] = None


class Test4MaxOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test1Id: Optional[SortOrder] = None
    test2Id: Optional[SortOrder] = None
    test3Id: Optional[SortOrder] = None
    test5Id: Optional[SortOrder] = None


class Test4MinOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test1Id: Optional[SortOrder] = None
    test2Id: Optional[SortOrder] = None
    test3Id: Optional[SortOrder] = None
    test5Id: Optional[SortOrder] = None


class Test4OrderByRelationAggregateInput(BaseModel):
    count: Optional[SortOrder] = Field(alias="_count", default=None)


class Test4OrderByWithAggregationInput(BaseModel):
    count: Optional["Test4CountOrderByAggregateInput"] = Field(
        alias="_count", default=None
    )
    max: Optional["Test4MaxOrderByAggregateInput"] = Field(alias="_max", default=None)
    min: Optional["Test4MinOrderByAggregateInput"] = Field(alias="_min", default=None)
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test1Id: Optional[SortOrder] = None
    test2Id: Optional[SortOrder] = None
    test3Id: Optional[SortOrder] = None
    test5Id: Optional[SortOrder] = None


class Test4OrderByWithRelationInput(BaseModel):
    createdBy: Optional["UserOrderByWithRelationInput"] = None
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test1: Optional["Test1OrderByWithRelationInput"] = None
    test1Id: Optional[SortOrder] = None
    test2: Optional["Test2OrderByWithRelationInput"] = None
    test2Id: Optional[SortOrder] = None
    test3: Optional["Test3OrderByWithRelationInput"] = None
    test3Id: Optional[SortOrder] = None
    test5: Optional["Test5OrderByWithRelationInput"] = None
    test5Id: Optional[SortOrder] = None


class Test4ScalarWhereInput(BaseModel):
    AND: Optional[List["Test4ScalarWhereInput"]] = None
    NOT: Optional[List["Test4ScalarWhereInput"]] = None
    OR: Optional[List["Test4ScalarWhereInput"]] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None
    test1Id: Optional["StringNullableFilter"] = None
    test2Id: Optional["StringFilter"] = None
    test3Id: Optional["StringFilter"] = None
    test5Id: Optional["StringNullableFilter"] = None


class Test4ScalarWhereWithAggregatesInput(BaseModel):
    AND: Optional[List["Test4ScalarWhereWithAggregatesInput"]] = None
    NOT: Optional[List["Test4ScalarWhereWithAggregatesInput"]] = None
    OR: Optional[List["Test4ScalarWhereWithAggregatesInput"]] = None
    createdById: Optional["StringNullableWithAggregatesFilter"] = None
    id: Optional["StringWithAggregatesFilter"] = None
    name: Optional["StringWithAggregatesFilter"] = None
    test1Id: Optional["StringNullableWithAggregatesFilter"] = None
    test2Id: Optional["StringWithAggregatesFilter"] = None
    test3Id: Optional["StringWithAggregatesFilter"] = None
    test5Id: Optional["StringNullableWithAggregatesFilter"] = None


class Test4UpdateInput(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest4NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateOneWithoutTest4NestedInput"] = None
    test2: Optional["Test2UpdateOneWithoutTest4NestedInput"] = None
    test3: Optional["Test3UpdateOneRequiredWithoutTest4NestedInput"] = None
    test5: Optional["Test5UpdateOneWithoutTest4NestedInput"] = None


class Test4UpdateManyMutationInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None


class Test4UpdateManyWithWhereWithoutCreatedByInput(BaseModel):
    data: "Test4UpdateManyMutationInput"
    where: "Test4ScalarWhereInput"


class Test4UpdateManyWithWhereWithoutTest1Input(BaseModel):
    data: "Test4UpdateManyMutationInput"
    where: "Test4ScalarWhereInput"


class Test4UpdateManyWithWhereWithoutTest2Input(BaseModel):
    data: "Test4UpdateManyMutationInput"
    where: "Test4ScalarWhereInput"


class Test4UpdateManyWithWhereWithoutTest3Input(BaseModel):
    data: "Test4UpdateManyMutationInput"
    where: "Test4ScalarWhereInput"


class Test4UpdateManyWithWhereWithoutTest5Input(BaseModel):
    data: "Test4UpdateManyMutationInput"
    where: "Test4ScalarWhereInput"


class Test4UpdateManyWithoutCreatedByNestedInput(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test4CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test4CreateManyCreatedByInputEnvelope"] = None
    delete: Optional[List["Test4WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test4ScalarWhereInput"]] = None
    disconnect: Optional[List["Test4WhereUniqueInput"]] = None
    set: Optional[List["Test4WhereUniqueInput"]] = None
    update: Optional[List["Test4UpdateWithWhereUniqueWithoutCreatedByInput"]] = None
    updateMany: Optional[List["Test4UpdateManyWithWhereWithoutCreatedByInput"]] = None
    upsert: Optional[List["Test4UpsertWithWhereUniqueWithoutCreatedByInput"]] = None


class Test4UpdateManyWithoutTest1NestedInput(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutTest1Input"]] = None
    create: Optional[List["Test4CreateWithoutTest1Input"]] = None
    createMany: Optional["Test4CreateManyTest1InputEnvelope"] = None
    delete: Optional[List["Test4WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test4ScalarWhereInput"]] = None
    disconnect: Optional[List["Test4WhereUniqueInput"]] = None
    set: Optional[List["Test4WhereUniqueInput"]] = None
    update: Optional[List["Test4UpdateWithWhereUniqueWithoutTest1Input"]] = None
    updateMany: Optional[List["Test4UpdateManyWithWhereWithoutTest1Input"]] = None
    upsert: Optional[List["Test4UpsertWithWhereUniqueWithoutTest1Input"]] = None


class Test4UpdateManyWithoutTest2NestedInput(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutTest2Input"]] = None
    create: Optional[List["Test4CreateWithoutTest2Input"]] = None
    createMany: Optional["Test4CreateManyTest2InputEnvelope"] = None
    delete: Optional[List["Test4WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test4ScalarWhereInput"]] = None
    disconnect: Optional[List["Test4WhereUniqueInput"]] = None
    set: Optional[List["Test4WhereUniqueInput"]] = None
    update: Optional[List["Test4UpdateWithWhereUniqueWithoutTest2Input"]] = None
    updateMany: Optional[List["Test4UpdateManyWithWhereWithoutTest2Input"]] = None
    upsert: Optional[List["Test4UpsertWithWhereUniqueWithoutTest2Input"]] = None


class Test4UpdateManyWithoutTest3NestedInput(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutTest3Input"]] = None
    create: Optional[List["Test4CreateWithoutTest3Input"]] = None
    createMany: Optional["Test4CreateManyTest3InputEnvelope"] = None
    delete: Optional[List["Test4WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test4ScalarWhereInput"]] = None
    disconnect: Optional[List["Test4WhereUniqueInput"]] = None
    set: Optional[List["Test4WhereUniqueInput"]] = None
    update: Optional[List["Test4UpdateWithWhereUniqueWithoutTest3Input"]] = None
    updateMany: Optional[List["Test4UpdateManyWithWhereWithoutTest3Input"]] = None
    upsert: Optional[List["Test4UpsertWithWhereUniqueWithoutTest3Input"]] = None


class Test4UpdateManyWithoutTest5NestedInput(BaseModel):
    connect: Optional[List["Test4WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test4CreateOrConnectWithoutTest5Input"]] = None
    create: Optional[List["Test4CreateWithoutTest5Input"]] = None
    createMany: Optional["Test4CreateManyTest5InputEnvelope"] = None
    delete: Optional[List["Test4WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test4ScalarWhereInput"]] = None
    disconnect: Optional[List["Test4WhereUniqueInput"]] = None
    set: Optional[List["Test4WhereUniqueInput"]] = None
    update: Optional[List["Test4UpdateWithWhereUniqueWithoutTest5Input"]] = None
    updateMany: Optional[List["Test4UpdateManyWithWhereWithoutTest5Input"]] = None
    upsert: Optional[List["Test4UpsertWithWhereUniqueWithoutTest5Input"]] = None


class Test4UpdateWithWhereUniqueWithoutCreatedByInput(BaseModel):
    data: "Test4UpdateWithoutCreatedByInput"
    where: "Test4WhereUniqueInput"


class Test4UpdateWithWhereUniqueWithoutTest1Input(BaseModel):
    data: "Test4UpdateWithoutTest1Input"
    where: "Test4WhereUniqueInput"


class Test4UpdateWithWhereUniqueWithoutTest2Input(BaseModel):
    data: "Test4UpdateWithoutTest2Input"
    where: "Test4WhereUniqueInput"


class Test4UpdateWithWhereUniqueWithoutTest3Input(BaseModel):
    data: "Test4UpdateWithoutTest3Input"
    where: "Test4WhereUniqueInput"


class Test4UpdateWithWhereUniqueWithoutTest5Input(BaseModel):
    data: "Test4UpdateWithoutTest5Input"
    where: "Test4WhereUniqueInput"


class Test4UpdateWithoutCreatedByInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateOneWithoutTest4NestedInput"] = None
    test2: Optional["Test2UpdateOneWithoutTest4NestedInput"] = None
    test3: Optional["Test3UpdateOneRequiredWithoutTest4NestedInput"] = None
    test5: Optional["Test5UpdateOneWithoutTest4NestedInput"] = None


class Test4UpdateWithoutTest1Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest4NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test2: Optional["Test2UpdateOneWithoutTest4NestedInput"] = None
    test3: Optional["Test3UpdateOneRequiredWithoutTest4NestedInput"] = None
    test5: Optional["Test5UpdateOneWithoutTest4NestedInput"] = None


class Test4UpdateWithoutTest2Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest4NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateOneWithoutTest4NestedInput"] = None
    test3: Optional["Test3UpdateOneRequiredWithoutTest4NestedInput"] = None
    test5: Optional["Test5UpdateOneWithoutTest4NestedInput"] = None


class Test4UpdateWithoutTest3Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest4NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateOneWithoutTest4NestedInput"] = None
    test2: Optional["Test2UpdateOneWithoutTest4NestedInput"] = None
    test5: Optional["Test5UpdateOneWithoutTest4NestedInput"] = None


class Test4UpdateWithoutTest5Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest4NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateOneWithoutTest4NestedInput"] = None
    test2: Optional["Test2UpdateOneWithoutTest4NestedInput"] = None
    test3: Optional["Test3UpdateOneRequiredWithoutTest4NestedInput"] = None


class Test4UpsertWithWhereUniqueWithoutCreatedByInput(BaseModel):
    create: "Test4CreateWithoutCreatedByInput"
    update: "Test4UpdateWithoutCreatedByInput"
    where: "Test4WhereUniqueInput"


class Test4UpsertWithWhereUniqueWithoutTest1Input(BaseModel):
    create: "Test4CreateWithoutTest1Input"
    update: "Test4UpdateWithoutTest1Input"
    where: "Test4WhereUniqueInput"


class Test4UpsertWithWhereUniqueWithoutTest2Input(BaseModel):
    create: "Test4CreateWithoutTest2Input"
    update: "Test4UpdateWithoutTest2Input"
    where: "Test4WhereUniqueInput"


class Test4UpsertWithWhereUniqueWithoutTest3Input(BaseModel):
    create: "Test4CreateWithoutTest3Input"
    update: "Test4UpdateWithoutTest3Input"
    where: "Test4WhereUniqueInput"


class Test4UpsertWithWhereUniqueWithoutTest5Input(BaseModel):
    create: "Test4CreateWithoutTest5Input"
    update: "Test4UpdateWithoutTest5Input"
    where: "Test4WhereUniqueInput"


class Test4WhereInput(BaseModel):
    AND: Optional[List["Test4WhereInput"]] = None
    NOT: Optional[List["Test4WhereInput"]] = None
    OR: Optional[List["Test4WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None
    test1: Optional["Test1NullableRelationFilter"] = None
    test1Id: Optional["StringNullableFilter"] = None
    test2: Optional["Test2NullableRelationFilter"] = None
    test2Id: Optional["StringFilter"] = None
    test3: Optional["Test3RelationFilter"] = None
    test3Id: Optional["StringFilter"] = None
    test5: Optional["Test5NullableRelationFilter"] = None
    test5Id: Optional["StringNullableFilter"] = None


class Test4WhereUniqueInput(BaseModel):
    AND: Optional[List["Test4WhereInput"]] = None
    NOT: Optional[List["Test4WhereInput"]] = None
    OR: Optional[List["Test4WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional[str] = None
    name: Optional["StringFilter"] = None
    test1: Optional["Test1NullableRelationFilter"] = None
    test1Id: Optional["StringNullableFilter"] = None
    test2: Optional["Test2NullableRelationFilter"] = None
    test2Id: Optional["StringFilter"] = None
    test3: Optional["Test3RelationFilter"] = None
    test3Id: Optional["StringFilter"] = None
    test5: Optional["Test5NullableRelationFilter"] = None
    test5Id: Optional["StringNullableFilter"] = None


class Test5CountOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test5CreateInput(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest5Input"] = None
    id: Optional[str] = None
    name: str
    test3: Optional["Test3CreateNestedManyWithoutTest5Input"] = None
    test4: Optional["Test4CreateNestedManyWithoutTest5Input"] = None


class Test5CreateManyCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str


class Test5CreateManyCreatedByInputEnvelope(BaseModel):
    data: List["Test5CreateManyCreatedByInput"]


class Test5CreateManyInput(BaseModel):
    createdById: Optional[str] = None
    id: Optional[str] = None
    name: str


class Test5CreateNestedManyWithoutCreatedByInput(BaseModel):
    connect: Optional[List["Test5WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test5CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test5CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test5CreateManyCreatedByInputEnvelope"] = None


class Test5CreateNestedOneWithoutTest3Input(BaseModel):
    connect: Optional["Test5WhereUniqueInput"] = None
    connectOrCreate: Optional["Test5CreateOrConnectWithoutTest3Input"] = None
    create: Optional["Test5CreateWithoutTest3Input"] = None


class Test5CreateNestedOneWithoutTest4Input(BaseModel):
    connect: Optional["Test5WhereUniqueInput"] = None
    connectOrCreate: Optional["Test5CreateOrConnectWithoutTest4Input"] = None
    create: Optional["Test5CreateWithoutTest4Input"] = None


class Test5CreateOrConnectWithoutCreatedByInput(BaseModel):
    create: "Test5CreateWithoutCreatedByInput"
    where: "Test5WhereUniqueInput"


class Test5CreateOrConnectWithoutTest3Input(BaseModel):
    create: "Test5CreateWithoutTest3Input"
    where: "Test5WhereUniqueInput"


class Test5CreateOrConnectWithoutTest4Input(BaseModel):
    create: "Test5CreateWithoutTest4Input"
    where: "Test5WhereUniqueInput"


class Test5CreateWithoutCreatedByInput(BaseModel):
    id: Optional[str] = None
    name: str
    test3: Optional["Test3CreateNestedManyWithoutTest5Input"] = None
    test4: Optional["Test4CreateNestedManyWithoutTest5Input"] = None


class Test5CreateWithoutTest3Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest5Input"] = None
    id: Optional[str] = None
    name: str
    test4: Optional["Test4CreateNestedManyWithoutTest5Input"] = None


class Test5CreateWithoutTest4Input(BaseModel):
    createdBy: Optional["UserCreateNestedOneWithoutTest5Input"] = None
    id: Optional[str] = None
    name: str
    test3: Optional["Test3CreateNestedManyWithoutTest5Input"] = None


class Test5ListRelationFilter(BaseModel):
    every: Optional["Test5WhereInput"] = None
    none: Optional["Test5WhereInput"] = None
    some: Optional["Test5WhereInput"] = None


class Test5MaxOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test5MinOrderByAggregateInput(BaseModel):
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test5NullableRelationFilter(BaseModel):
    is_: Optional["Test5WhereInput"] = Field(alias="is", default=None)
    isNot: Optional["Test5WhereInput"] = None


class Test5OrderByRelationAggregateInput(BaseModel):
    count: Optional[SortOrder] = Field(alias="_count", default=None)


class Test5OrderByWithAggregationInput(BaseModel):
    count: Optional["Test5CountOrderByAggregateInput"] = Field(
        alias="_count", default=None
    )
    max: Optional["Test5MaxOrderByAggregateInput"] = Field(alias="_max", default=None)
    min: Optional["Test5MinOrderByAggregateInput"] = Field(alias="_min", default=None)
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class Test5OrderByWithRelationInput(BaseModel):
    createdBy: Optional["UserOrderByWithRelationInput"] = None
    createdById: Optional[SortOrder] = None
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test3: Optional["Test3OrderByRelationAggregateInput"] = None
    test4: Optional["Test4OrderByRelationAggregateInput"] = None


class Test5RelationFilter(BaseModel):
    is_: Optional["Test5WhereInput"] = Field(alias="is", default=None)
    isNot: Optional["Test5WhereInput"] = None


class Test5ScalarWhereInput(BaseModel):
    AND: Optional[List["Test5ScalarWhereInput"]] = None
    NOT: Optional[List["Test5ScalarWhereInput"]] = None
    OR: Optional[List["Test5ScalarWhereInput"]] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None


class Test5ScalarWhereWithAggregatesInput(BaseModel):
    AND: Optional[List["Test5ScalarWhereWithAggregatesInput"]] = None
    NOT: Optional[List["Test5ScalarWhereWithAggregatesInput"]] = None
    OR: Optional[List["Test5ScalarWhereWithAggregatesInput"]] = None
    createdById: Optional["StringNullableWithAggregatesFilter"] = None
    id: Optional["StringWithAggregatesFilter"] = None
    name: Optional["StringWithAggregatesFilter"] = None


class Test5UpdateInput(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest5NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test3: Optional["Test3UpdateManyWithoutTest5NestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest5NestedInput"] = None


class Test5UpdateManyMutationInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None


class Test5UpdateManyWithWhereWithoutCreatedByInput(BaseModel):
    data: "Test5UpdateManyMutationInput"
    where: "Test5ScalarWhereInput"


class Test5UpdateManyWithoutCreatedByNestedInput(BaseModel):
    connect: Optional[List["Test5WhereUniqueInput"]] = None
    connectOrCreate: Optional[List["Test5CreateOrConnectWithoutCreatedByInput"]] = None
    create: Optional[List["Test5CreateWithoutCreatedByInput"]] = None
    createMany: Optional["Test5CreateManyCreatedByInputEnvelope"] = None
    delete: Optional[List["Test5WhereUniqueInput"]] = None
    deleteMany: Optional[List["Test5ScalarWhereInput"]] = None
    disconnect: Optional[List["Test5WhereUniqueInput"]] = None
    set: Optional[List["Test5WhereUniqueInput"]] = None
    update: Optional[List["Test5UpdateWithWhereUniqueWithoutCreatedByInput"]] = None
    updateMany: Optional[List["Test5UpdateManyWithWhereWithoutCreatedByInput"]] = None
    upsert: Optional[List["Test5UpsertWithWhereUniqueWithoutCreatedByInput"]] = None


class Test5UpdateOneRequiredWithoutTest3NestedInput(BaseModel):
    connect: Optional["Test5WhereUniqueInput"] = None
    connectOrCreate: Optional["Test5CreateOrConnectWithoutTest3Input"] = None
    create: Optional["Test5CreateWithoutTest3Input"] = None
    update: Optional["Test5UpdateToOneWithWhereWithoutTest3Input"] = None
    upsert: Optional["Test5UpsertWithoutTest3Input"] = None


class Test5UpdateOneWithoutTest4NestedInput(BaseModel):
    connect: Optional["Test5WhereUniqueInput"] = None
    connectOrCreate: Optional["Test5CreateOrConnectWithoutTest4Input"] = None
    create: Optional["Test5CreateWithoutTest4Input"] = None
    delete: Optional["Test5WhereInput"] = None
    disconnect: Optional[bool] = None
    update: Optional["Test5UpdateToOneWithWhereWithoutTest4Input"] = None
    upsert: Optional["Test5UpsertWithoutTest4Input"] = None


class Test5UpdateToOneWithWhereWithoutTest3Input(BaseModel):
    data: "Test5UpdateWithoutTest3Input"
    where: Optional["Test5WhereInput"] = None


class Test5UpdateToOneWithWhereWithoutTest4Input(BaseModel):
    data: "Test5UpdateWithoutTest4Input"
    where: Optional["Test5WhereInput"] = None


class Test5UpdateWithWhereUniqueWithoutCreatedByInput(BaseModel):
    data: "Test5UpdateWithoutCreatedByInput"
    where: "Test5WhereUniqueInput"


class Test5UpdateWithoutCreatedByInput(BaseModel):
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test3: Optional["Test3UpdateManyWithoutTest5NestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest5NestedInput"] = None


class Test5UpdateWithoutTest3Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest5NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test4: Optional["Test4UpdateManyWithoutTest5NestedInput"] = None


class Test5UpdateWithoutTest4Input(BaseModel):
    createdBy: Optional["UserUpdateOneWithoutTest5NestedInput"] = None
    name: Optional["StringFieldUpdateOperationsInput"] = None
    test3: Optional["Test3UpdateManyWithoutTest5NestedInput"] = None


class Test5UpsertWithWhereUniqueWithoutCreatedByInput(BaseModel):
    create: "Test5CreateWithoutCreatedByInput"
    update: "Test5UpdateWithoutCreatedByInput"
    where: "Test5WhereUniqueInput"


class Test5UpsertWithoutTest3Input(BaseModel):
    create: "Test5CreateWithoutTest3Input"
    update: "Test5UpdateWithoutTest3Input"
    where: Optional["Test5WhereInput"] = None


class Test5UpsertWithoutTest4Input(BaseModel):
    create: "Test5CreateWithoutTest4Input"
    update: "Test5UpdateWithoutTest4Input"
    where: Optional["Test5WhereInput"] = None


class Test5WhereInput(BaseModel):
    AND: Optional[List["Test5WhereInput"]] = None
    NOT: Optional[List["Test5WhereInput"]] = None
    OR: Optional[List["Test5WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringFilter"] = None
    test3: Optional["Test3ListRelationFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None


class Test5WhereUniqueInput(BaseModel):
    AND: Optional[List["Test5WhereInput"]] = None
    NOT: Optional[List["Test5WhereInput"]] = None
    OR: Optional[List["Test5WhereInput"]] = None
    createdBy: Optional["UserNullableRelationFilter"] = None
    createdById: Optional["StringNullableFilter"] = None
    id: Optional[str] = None
    name: Optional["StringFilter"] = None
    test3: Optional["Test3ListRelationFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None


class UserCountOrderByAggregateInput(BaseModel):
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class UserCreateInput(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    test1: Optional["Test1CreateNestedManyWithoutCreatedByInput"] = None
    test2: Optional["Test2CreateNestedManyWithoutCreatedByInput"] = None
    test3: Optional["Test3CreateNestedManyWithoutCreatedByInput"] = None
    test4: Optional["Test4CreateNestedManyWithoutCreatedByInput"] = None
    test5: Optional["Test5CreateNestedManyWithoutCreatedByInput"] = None


class UserCreateManyInput(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None


class UserCreateNestedOneWithoutTest1Input(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest1Input"] = None
    create: Optional["UserCreateWithoutTest1Input"] = None


class UserCreateNestedOneWithoutTest2Input(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest2Input"] = None
    create: Optional["UserCreateWithoutTest2Input"] = None


class UserCreateNestedOneWithoutTest3Input(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest3Input"] = None
    create: Optional["UserCreateWithoutTest3Input"] = None


class UserCreateNestedOneWithoutTest4Input(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest4Input"] = None
    create: Optional["UserCreateWithoutTest4Input"] = None


class UserCreateNestedOneWithoutTest5Input(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest5Input"] = None
    create: Optional["UserCreateWithoutTest5Input"] = None


class UserCreateOrConnectWithoutTest1Input(BaseModel):
    create: "UserCreateWithoutTest1Input"
    where: "UserWhereUniqueInput"


class UserCreateOrConnectWithoutTest2Input(BaseModel):
    create: "UserCreateWithoutTest2Input"
    where: "UserWhereUniqueInput"


class UserCreateOrConnectWithoutTest3Input(BaseModel):
    create: "UserCreateWithoutTest3Input"
    where: "UserWhereUniqueInput"


class UserCreateOrConnectWithoutTest4Input(BaseModel):
    create: "UserCreateWithoutTest4Input"
    where: "UserWhereUniqueInput"


class UserCreateOrConnectWithoutTest5Input(BaseModel):
    create: "UserCreateWithoutTest5Input"
    where: "UserWhereUniqueInput"


class UserCreateWithoutTest1Input(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    test2: Optional["Test2CreateNestedManyWithoutCreatedByInput"] = None
    test3: Optional["Test3CreateNestedManyWithoutCreatedByInput"] = None
    test4: Optional["Test4CreateNestedManyWithoutCreatedByInput"] = None
    test5: Optional["Test5CreateNestedManyWithoutCreatedByInput"] = None


class UserCreateWithoutTest2Input(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    test1: Optional["Test1CreateNestedManyWithoutCreatedByInput"] = None
    test3: Optional["Test3CreateNestedManyWithoutCreatedByInput"] = None
    test4: Optional["Test4CreateNestedManyWithoutCreatedByInput"] = None
    test5: Optional["Test5CreateNestedManyWithoutCreatedByInput"] = None


class UserCreateWithoutTest3Input(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    test1: Optional["Test1CreateNestedManyWithoutCreatedByInput"] = None
    test2: Optional["Test2CreateNestedManyWithoutCreatedByInput"] = None
    test4: Optional["Test4CreateNestedManyWithoutCreatedByInput"] = None
    test5: Optional["Test5CreateNestedManyWithoutCreatedByInput"] = None


class UserCreateWithoutTest4Input(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    test1: Optional["Test1CreateNestedManyWithoutCreatedByInput"] = None
    test2: Optional["Test2CreateNestedManyWithoutCreatedByInput"] = None
    test3: Optional["Test3CreateNestedManyWithoutCreatedByInput"] = None
    test5: Optional["Test5CreateNestedManyWithoutCreatedByInput"] = None


class UserCreateWithoutTest5Input(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    test1: Optional["Test1CreateNestedManyWithoutCreatedByInput"] = None
    test2: Optional["Test2CreateNestedManyWithoutCreatedByInput"] = None
    test3: Optional["Test3CreateNestedManyWithoutCreatedByInput"] = None
    test4: Optional["Test4CreateNestedManyWithoutCreatedByInput"] = None


class UserMaxOrderByAggregateInput(BaseModel):
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class UserMinOrderByAggregateInput(BaseModel):
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class UserNullableRelationFilter(BaseModel):
    is_: Optional["UserWhereInput"] = Field(alias="is", default=None)
    isNot: Optional["UserWhereInput"] = None


class UserOrderByWithAggregationInput(BaseModel):
    count: Optional["UserCountOrderByAggregateInput"] = Field(
        alias="_count", default=None
    )
    max: Optional["UserMaxOrderByAggregateInput"] = Field(alias="_max", default=None)
    min: Optional["UserMinOrderByAggregateInput"] = Field(alias="_min", default=None)
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None


class UserOrderByWithRelationInput(BaseModel):
    id: Optional[SortOrder] = None
    name: Optional[SortOrder] = None
    test1: Optional["Test1OrderByRelationAggregateInput"] = None
    test2: Optional["Test2OrderByRelationAggregateInput"] = None
    test3: Optional["Test3OrderByRelationAggregateInput"] = None
    test4: Optional["Test4OrderByRelationAggregateInput"] = None
    test5: Optional["Test5OrderByRelationAggregateInput"] = None


class UserScalarWhereWithAggregatesInput(BaseModel):
    AND: Optional[List["UserScalarWhereWithAggregatesInput"]] = None
    NOT: Optional[List["UserScalarWhereWithAggregatesInput"]] = None
    OR: Optional[List["UserScalarWhereWithAggregatesInput"]] = None
    id: Optional["StringWithAggregatesFilter"] = None
    name: Optional["StringNullableWithAggregatesFilter"] = None


class UserUpdateInput(BaseModel):
    name: Optional["NullableStringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateManyWithoutCreatedByNestedInput"] = None
    test2: Optional["Test2UpdateManyWithoutCreatedByNestedInput"] = None
    test3: Optional["Test3UpdateManyWithoutCreatedByNestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutCreatedByNestedInput"] = None
    test5: Optional["Test5UpdateManyWithoutCreatedByNestedInput"] = None


class UserUpdateManyMutationInput(BaseModel):
    name: Optional["NullableStringFieldUpdateOperationsInput"] = None


class UserUpdateOneWithoutTest1NestedInput(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest1Input"] = None
    create: Optional["UserCreateWithoutTest1Input"] = None
    delete: Optional["UserWhereInput"] = None
    disconnect: Optional[bool] = None
    update: Optional["UserUpdateToOneWithWhereWithoutTest1Input"] = None
    upsert: Optional["UserUpsertWithoutTest1Input"] = None


class UserUpdateOneWithoutTest2NestedInput(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest2Input"] = None
    create: Optional["UserCreateWithoutTest2Input"] = None
    delete: Optional["UserWhereInput"] = None
    disconnect: Optional[bool] = None
    update: Optional["UserUpdateToOneWithWhereWithoutTest2Input"] = None
    upsert: Optional["UserUpsertWithoutTest2Input"] = None


class UserUpdateOneWithoutTest3NestedInput(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest3Input"] = None
    create: Optional["UserCreateWithoutTest3Input"] = None
    delete: Optional["UserWhereInput"] = None
    disconnect: Optional[bool] = None
    update: Optional["UserUpdateToOneWithWhereWithoutTest3Input"] = None
    upsert: Optional["UserUpsertWithoutTest3Input"] = None


class UserUpdateOneWithoutTest4NestedInput(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest4Input"] = None
    create: Optional["UserCreateWithoutTest4Input"] = None
    delete: Optional["UserWhereInput"] = None
    disconnect: Optional[bool] = None
    update: Optional["UserUpdateToOneWithWhereWithoutTest4Input"] = None
    upsert: Optional["UserUpsertWithoutTest4Input"] = None


class UserUpdateOneWithoutTest5NestedInput(BaseModel):
    connect: Optional["UserWhereUniqueInput"] = None
    connectOrCreate: Optional["UserCreateOrConnectWithoutTest5Input"] = None
    create: Optional["UserCreateWithoutTest5Input"] = None
    delete: Optional["UserWhereInput"] = None
    disconnect: Optional[bool] = None
    update: Optional["UserUpdateToOneWithWhereWithoutTest5Input"] = None
    upsert: Optional["UserUpsertWithoutTest5Input"] = None


class UserUpdateToOneWithWhereWithoutTest1Input(BaseModel):
    data: "UserUpdateWithoutTest1Input"
    where: Optional["UserWhereInput"] = None


class UserUpdateToOneWithWhereWithoutTest2Input(BaseModel):
    data: "UserUpdateWithoutTest2Input"
    where: Optional["UserWhereInput"] = None


class UserUpdateToOneWithWhereWithoutTest3Input(BaseModel):
    data: "UserUpdateWithoutTest3Input"
    where: Optional["UserWhereInput"] = None


class UserUpdateToOneWithWhereWithoutTest4Input(BaseModel):
    data: "UserUpdateWithoutTest4Input"
    where: Optional["UserWhereInput"] = None


class UserUpdateToOneWithWhereWithoutTest5Input(BaseModel):
    data: "UserUpdateWithoutTest5Input"
    where: Optional["UserWhereInput"] = None


class UserUpdateWithoutTest1Input(BaseModel):
    name: Optional["NullableStringFieldUpdateOperationsInput"] = None
    test2: Optional["Test2UpdateManyWithoutCreatedByNestedInput"] = None
    test3: Optional["Test3UpdateManyWithoutCreatedByNestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutCreatedByNestedInput"] = None
    test5: Optional["Test5UpdateManyWithoutCreatedByNestedInput"] = None


class UserUpdateWithoutTest2Input(BaseModel):
    name: Optional["NullableStringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateManyWithoutCreatedByNestedInput"] = None
    test3: Optional["Test3UpdateManyWithoutCreatedByNestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutCreatedByNestedInput"] = None
    test5: Optional["Test5UpdateManyWithoutCreatedByNestedInput"] = None


class UserUpdateWithoutTest3Input(BaseModel):
    name: Optional["NullableStringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateManyWithoutCreatedByNestedInput"] = None
    test2: Optional["Test2UpdateManyWithoutCreatedByNestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutCreatedByNestedInput"] = None
    test5: Optional["Test5UpdateManyWithoutCreatedByNestedInput"] = None


class UserUpdateWithoutTest4Input(BaseModel):
    name: Optional["NullableStringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateManyWithoutCreatedByNestedInput"] = None
    test2: Optional["Test2UpdateManyWithoutCreatedByNestedInput"] = None
    test3: Optional["Test3UpdateManyWithoutCreatedByNestedInput"] = None
    test5: Optional["Test5UpdateManyWithoutCreatedByNestedInput"] = None


class UserUpdateWithoutTest5Input(BaseModel):
    name: Optional["NullableStringFieldUpdateOperationsInput"] = None
    test1: Optional["Test1UpdateManyWithoutCreatedByNestedInput"] = None
    test2: Optional["Test2UpdateManyWithoutCreatedByNestedInput"] = None
    test3: Optional["Test3UpdateManyWithoutCreatedByNestedInput"] = None
    test4: Optional["Test4UpdateManyWithoutCreatedByNestedInput"] = None


class UserUpsertWithoutTest1Input(BaseModel):
    create: "UserCreateWithoutTest1Input"
    update: "UserUpdateWithoutTest1Input"
    where: Optional["UserWhereInput"] = None


class UserUpsertWithoutTest2Input(BaseModel):
    create: "UserCreateWithoutTest2Input"
    update: "UserUpdateWithoutTest2Input"
    where: Optional["UserWhereInput"] = None


class UserUpsertWithoutTest3Input(BaseModel):
    create: "UserCreateWithoutTest3Input"
    update: "UserUpdateWithoutTest3Input"
    where: Optional["UserWhereInput"] = None


class UserUpsertWithoutTest4Input(BaseModel):
    create: "UserCreateWithoutTest4Input"
    update: "UserUpdateWithoutTest4Input"
    where: Optional["UserWhereInput"] = None


class UserUpsertWithoutTest5Input(BaseModel):
    create: "UserCreateWithoutTest5Input"
    update: "UserUpdateWithoutTest5Input"
    where: Optional["UserWhereInput"] = None


class UserWhereInput(BaseModel):
    AND: Optional[List["UserWhereInput"]] = None
    NOT: Optional[List["UserWhereInput"]] = None
    OR: Optional[List["UserWhereInput"]] = None
    id: Optional["StringFilter"] = None
    name: Optional["StringNullableFilter"] = None
    test1: Optional["Test1ListRelationFilter"] = None
    test2: Optional["Test2ListRelationFilter"] = None
    test3: Optional["Test3ListRelationFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None
    test5: Optional["Test5ListRelationFilter"] = None


class UserWhereUniqueInput(BaseModel):
    AND: Optional[List["UserWhereInput"]] = None
    NOT: Optional[List["UserWhereInput"]] = None
    OR: Optional[List["UserWhereInput"]] = None
    id: Optional[str] = None
    name: Optional["StringNullableFilter"] = None
    test1: Optional["Test1ListRelationFilter"] = None
    test2: Optional["Test2ListRelationFilter"] = None
    test3: Optional["Test3ListRelationFilter"] = None
    test4: Optional["Test4ListRelationFilter"] = None
    test5: Optional["Test5ListRelationFilter"] = None

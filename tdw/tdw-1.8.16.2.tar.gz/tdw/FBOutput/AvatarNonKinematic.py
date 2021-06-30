# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class AvatarNonKinematic(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAvatarNonKinematic(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = AvatarNonKinematic()
        x.Init(buf, n + offset)
        return x

    # AvatarNonKinematic
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # AvatarNonKinematic
    def Id(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AvatarNonKinematic
    def Position(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AvatarNonKinematic
    def Rotation(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .Quaternion import Quaternion
            obj = Quaternion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AvatarNonKinematic
    def Forward(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AvatarNonKinematic
    def Velocity(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AvatarNonKinematic
    def AngularVelocity(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3 import Vector3
            obj = Vector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AvatarNonKinematic
    def Mass(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(tdw.flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AvatarNonKinematic
    def Sleeping(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(tdw.flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def AvatarNonKinematicStart(builder): builder.StartObject(8)
def AvatarNonKinematicAddId(builder, id): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def AvatarNonKinematicAddPosition(builder, position): builder.PrependStructSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(position), 0)
def AvatarNonKinematicAddRotation(builder, rotation): builder.PrependStructSlot(2, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(rotation), 0)
def AvatarNonKinematicAddForward(builder, forward): builder.PrependStructSlot(3, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(forward), 0)
def AvatarNonKinematicAddVelocity(builder, velocity): builder.PrependStructSlot(4, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(velocity), 0)
def AvatarNonKinematicAddAngularVelocity(builder, angularVelocity): builder.PrependStructSlot(5, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(angularVelocity), 0)
def AvatarNonKinematicAddMass(builder, mass): builder.PrependFloat32Slot(6, mass, 0.0)
def AvatarNonKinematicAddSleeping(builder, sleeping): builder.PrependBoolSlot(7, sleeping, 0)
def AvatarNonKinematicEnd(builder): return builder.EndObject()


from quakeio.core import GroundMotionComponent, GroundMotionEvent
from quakeio.utils.parseutils import open_quake
import numpy

def read(read_file,**kwds):
    with open_quake(read_file) as f:
        pass

def write(write_file, ground_motion, **kwds):
    #print(type(ground_motion))
    if isinstance(ground_motion,GroundMotionComponent):
        accel = numpy.asarray(ground_motion.accel)[:,None]
    else:
        raise ValueError(
            f"Cannot conver motion of type `{type(ground_motion)}` to GroundMotionComponent"
        )
    with open_quake(write_file,"w") as f:
        numpy.savetxt(f, accel, fmt="%.8f")#delimiter="\n")


FILE_TYPES = {
        "opensees": {"write": write, "type": "any"}
}


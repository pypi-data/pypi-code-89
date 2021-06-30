import cv2
import numpy
from draugr.opencv_utilities.dlib.dlib_utilities import (
    Dlib5faciallandmarksindices,
    Dlib68faciallandmarksindices,
    shape_to_ndarray,
)

__all__ = ["align_face"]


def align_face(
    image,
    gray,
    rect,
    predictor,
    desired_left_eye=(0.35, 0.35),
    desired_face_size=(256, 256),
):
    desired_face_width, desired_face_height = desired_face_size
    face_shape = shape_to_ndarray(predictor(gray, rect))

    if len(face_shape) == 68:
        slicer = Dlib68faciallandmarksindices
    else:
        slicer = Dlib5faciallandmarksindices

    left_eye_pts = slicer.slice(face_shape, slicer.left_eye)
    right_eye_pts = slicer.slice(face_shape, slicer.right_eye)

    # compute the center of mass for each eye
    left_eye_center = left_eye_pts.mean(axis=0).astype(numpy.int)
    right_eye_center = right_eye_pts.mean(axis=0).astype(numpy.int)

    # compute the angle between the eye centroids
    d_y = right_eye_center[1] - left_eye_center[1]
    d_x = right_eye_center[0] - left_eye_center[0]
    angle = (numpy.degrees(numpy.arctan2(d_y, d_x)) - 180).item()

    # compute the desired right eye x-coordinate based on the
    # desired x-coordinate of the left eye
    desired_right_eye_x = 1.0 - desired_left_eye[0]

    # determine the scale of the new resulting image by taking
    # the ratio of the distance between eyes in the *current*
    # image to the ratio of distance between eyes in the
    # *desired* image
    dist = numpy.sqrt((d_x ** 2) + (d_y ** 2))
    desired_dist = desired_right_eye_x - desired_left_eye[0]
    desired_dist *= desired_face_width
    scale = (desired_dist / dist).item()

    # compute center (x, y)-coordinates (i.e., the median point)
    # between the two eyes in the input image
    eyes_center = (
        ((left_eye_center[0] + right_eye_center[0]) // 2).item(),
        ((left_eye_center[1] + right_eye_center[1]) // 2).item(),
    )

    rot_m = cv2.getRotationMatrix2D(
        eyes_center, angle, scale
    )  # grab the rotation matrix for rotating and scaling the face

    # update the translation component of the matrix
    t_x = desired_face_width * 0.5
    t_y = desired_face_height * desired_left_eye[1]
    rot_m[0, 2] += t_x - eyes_center[0]
    rot_m[1, 2] += t_y - eyes_center[1]

    return cv2.warpAffine(
        image, rot_m, (desired_face_width, desired_face_height), flags=cv2.INTER_CUBIC
    )  # apply the affine transformation

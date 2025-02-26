cmake_minimum_required(VERSION 3.5)
project(chemistry_laboratory)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find ament_cmake and other dependencies
find_package(ament_cmake REQUIRED)


ament_package(
#  INCLUDE_DIRS include
#  LIBRARIES chemistry_laboratory
#  DEPENDS other_ament_pkg
)

#############
## Install ##
#############

# Install launch files
install(DIRECTORY
  launch
  meshes
  urdf
  rviz
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
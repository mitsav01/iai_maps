cmake_minimum_required(VERSION 3.5)
project(iai_dlr_cutting_demo)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config doc launch urdf rviz2
  DESTINATION share/${PROJECT_NAME})

ament_package()
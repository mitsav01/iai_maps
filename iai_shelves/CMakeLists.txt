cmake_minimum_required(VERSION 2.8.3)
project(iai_shelves)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch maps urdf meshes
  DESTINATION share/${PROJECT_NAME})

ament_package()
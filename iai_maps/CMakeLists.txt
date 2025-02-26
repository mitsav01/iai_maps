cmake_minimum_required(VERSION 3.5)
project(iai_maps)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch maps
  DESTINATION share/${PROJECT_NAME})

ament_package()
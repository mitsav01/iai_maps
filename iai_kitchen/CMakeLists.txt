cmake_minimum_required(VERSION 3.5)
project(iai_kitchen)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch meshes owl urdf urdf_obj worlds
        DESTINATION share/${PROJECT_NAME})

ament_package()
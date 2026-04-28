cmake_minimum_required(VERSION 3.16)

project(Final_assignement_Mbock_Lignac LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(Final_assignement_Mbock_Lignac nombre.cpp)

include(GNUInstallDirs)
install(TARGETS Final_assignement_Mbock_Lignac
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

cmake_minimum_required(VERSION 3.16)

project(assignement_mbock_lignac LANGUAGES C)

add_executable(assignement_mbock_lignac main.c)

include(GNUInstallDirs)
install(TARGETS assignement_mbock_lignac
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

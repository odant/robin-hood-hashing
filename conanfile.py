from conan import ConanFile, tools
from conan.errors import ConanInvalidConfiguration
import shutil
import os

required_conan_version = ">=1.60.0"

class GoogleBenchmarkConan(ConanFile):
    name = "robin-hood-hashing"
    version = "3.11.5+0"
    description = "Fast & memory efficient hashtable based on robin hood hashing for C++11/14/17/20"
    url = "https://github.com/martinus/robin-hood-hashing"
    homepage = "https://github.com/martinus/robin-hood-hashing"
    author = "Martin Ankerl"
    license = "MIT License"
    exports_sources = ["*"]
    no_copy_source = True
    settings = "os", "compiler", "build_type", "arch"
    package_type = "header-library"

    def layout(self):
        tools.cmake.cmake_layout(self)
        
    def generate(self):
        tc = tools.cmake.CMakeToolchain(self)
        tc.variables["RH_STANDALONE_PROJECT"] = "OFF"
        tc.generate()
        
    def build(self):
        cmake = tools.cmake.CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = tools.cmake.CMake(self)
        cmake.install()

    def package_id(self):
        self.info.clear()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "robin_hood")
        self.cpp_info.set_property("cmake_target_name", "robin_hood::robin_hood")
        self.cpp_info.libs = []
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []        

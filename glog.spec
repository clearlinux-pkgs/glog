#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glog
Version  : 0.6.0
Release  : 18
URL      : https://github.com/google/glog/archive/v0.6.0/glog-0.6.0.tar.gz
Source0  : https://github.com/google/glog/archive/v0.6.0/glog-0.6.0.tar.gz
Summary  : Google Log (glog) C++ logging framework
Group    : Development/Tools
License  : BSD-3-Clause
Requires: glog-lib = %{version}-%{release}
Requires: glog-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gflags-dev

%description
Google Logging Library
======================
|Linux Github actions| |Windows Github actions| |macOS Github actions| |Total alerts| |Language grade: C++| |Codecov|

%package dev
Summary: dev components for the glog package.
Group: Development
Requires: glog-lib = %{version}-%{release}
Provides: glog-devel = %{version}-%{release}
Requires: glog = %{version}-%{release}

%description dev
dev components for the glog package.


%package lib
Summary: lib components for the glog package.
Group: Libraries
Requires: glog-license = %{version}-%{release}

%description lib
lib components for the glog package.


%package license
Summary: license components for the glog package.
Group: Default

%description license
license components for the glog package.


%prep
%setup -q -n glog-0.6.0
cd %{_builddir}/glog-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656115145
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1656115145
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glog
cp %{_builddir}/glog-0.6.0/COPYING %{buildroot}/usr/share/package-licenses/glog/43c9d4e201bf773d965455b593cd8a244d98564b
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/glog/export.h
/usr/include/glog/log_severity.h
/usr/include/glog/logging.h
/usr/include/glog/platform.h
/usr/include/glog/raw_logging.h
/usr/include/glog/stl_logging.h
/usr/include/glog/vlog_is_on.h
/usr/lib64/cmake/glog/glog-config-version.cmake
/usr/lib64/cmake/glog/glog-config.cmake
/usr/lib64/cmake/glog/glog-modules.cmake
/usr/lib64/cmake/glog/glog-targets-relwithdebinfo.cmake
/usr/lib64/cmake/glog/glog-targets.cmake
/usr/lib64/libglog.so
/usr/lib64/pkgconfig/libglog.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libglog.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libglog.so.0.6.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libglog.so.1
/usr/lib64/libglog.so.0.6.0
/usr/lib64/libglog.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glog/43c9d4e201bf773d965455b593cd8a244d98564b

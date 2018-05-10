#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glog
Version  : 0.3.5
Release  : 11
URL      : https://github.com/google/glog/archive/v0.3.5.tar.gz
Source0  : https://github.com/google/glog/archive/v0.3.5.tar.gz
Summary  : A C++ application logging library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: glog-lib
Requires: glog-doc

%description
The %name package contains a library that implements application-level
logging.  This library provides logging APIs based on C++-style
streams and various helper macros.

%package dev
Summary: dev components for the glog package.
Group: Development
Requires: glog-lib
Provides: glog-devel

%description dev
dev components for the glog package.


%package doc
Summary: doc components for the glog package.
Group: Documentation

%description doc
doc components for the glog package.


%package lib
Summary: lib components for the glog package.
Group: Libraries

%description lib
lib components for the glog package.


%prep
%setup -q -n glog-0.3.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494343555
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1494343555
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/glog/log_severity.h
/usr/include/glog/logging.h
/usr/include/glog/raw_logging.h
/usr/include/glog/stl_logging.h
/usr/include/glog/vlog_is_on.h
/usr/lib64/libglog.so
/usr/lib64/pkgconfig/libglog.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/glog/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libglog.so.0
/usr/lib64/libglog.so.0.0.0

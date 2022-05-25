#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : amtk
Version  : 5.4.1
Release  : 12
URL      : https://download.gnome.org/sources/amtk/5.4/amtk-5.4.1.tar.xz
Source0  : https://download.gnome.org/sources/amtk/5.4/amtk-5.4.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: amtk-data = %{version}-%{release}
Requires: amtk-lib = %{version}-%{release}
Requires: amtk-license = %{version}-%{release}
Requires: amtk-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml

%description
Amtk - Actions, Menus and Toolbars Kit for GTK applications
===========================================================

%package data
Summary: data components for the amtk package.
Group: Data

%description data
data components for the amtk package.


%package dev
Summary: dev components for the amtk package.
Group: Development
Requires: amtk-lib = %{version}-%{release}
Requires: amtk-data = %{version}-%{release}
Provides: amtk-devel = %{version}-%{release}
Requires: amtk = %{version}-%{release}

%description dev
dev components for the amtk package.


%package doc
Summary: doc components for the amtk package.
Group: Documentation

%description doc
doc components for the amtk package.


%package lib
Summary: lib components for the amtk package.
Group: Libraries
Requires: amtk-data = %{version}-%{release}
Requires: amtk-license = %{version}-%{release}

%description lib
lib components for the amtk package.


%package license
Summary: license components for the amtk package.
Group: Default

%description license
license components for the amtk package.


%package locales
Summary: locales components for the amtk package.
Group: Default

%description locales
locales components for the amtk package.


%prep
%setup -q -n amtk-5.4.1
cd %{_builddir}/amtk-5.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653500974
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/amtk
cp %{_builddir}/amtk-5.4.1/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/amtk/757b86330df80f81143d5916b3e92b4bcb1b1890
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang amtk-5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Amtk-5.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/amtk-5/amtk/amtk-action-info-central-store.h
/usr/include/amtk-5/amtk/amtk-action-info-store.h
/usr/include/amtk-5/amtk/amtk-action-info.h
/usr/include/amtk-5/amtk/amtk-action-map.h
/usr/include/amtk-5/amtk/amtk-application-window.h
/usr/include/amtk-5/amtk/amtk-enum-types.h
/usr/include/amtk-5/amtk/amtk-factory.h
/usr/include/amtk-5/amtk/amtk-gmenu.h
/usr/include/amtk-5/amtk/amtk-init.h
/usr/include/amtk-5/amtk/amtk-menu-item.h
/usr/include/amtk-5/amtk/amtk-menu-shell.h
/usr/include/amtk-5/amtk/amtk-shortcuts.h
/usr/include/amtk-5/amtk/amtk-utils.h
/usr/include/amtk-5/amtk/amtk.h
/usr/lib64/libamtk-5.so
/usr/lib64/pkgconfig/amtk-5.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/amtk-5/AmtkActionInfo.html
/usr/share/gtk-doc/html/amtk-5/AmtkActionInfoCentralStore.html
/usr/share/gtk-doc/html/amtk-5/AmtkActionInfoStore.html
/usr/share/gtk-doc/html/amtk-5/AmtkApplicationWindow.html
/usr/share/gtk-doc/html/amtk-5/AmtkFactory.html
/usr/share/gtk-doc/html/amtk-5/AmtkMenuShell.html
/usr/share/gtk-doc/html/amtk-5/amtk-5-Amtk-Initialization-and-Finalization.html
/usr/share/gtk-doc/html/amtk-5/amtk-5-AmtkActionMap.html
/usr/share/gtk-doc/html/amtk-5/amtk-5-AmtkGmenu.html
/usr/share/gtk-doc/html/amtk-5/amtk-5-AmtkMenuItem.html
/usr/share/gtk-doc/html/amtk-5/amtk-5-AmtkShortcuts.html
/usr/share/gtk-doc/html/amtk-5/amtk-5-AmtkUtils.html
/usr/share/gtk-doc/html/amtk-5/amtk-5.devhelp2
/usr/share/gtk-doc/html/amtk-5/amtk-intro.html
/usr/share/gtk-doc/html/amtk-5/annexes.html
/usr/share/gtk-doc/html/amtk-5/annotation-glossary.html
/usr/share/gtk-doc/html/amtk-5/api-index-2-0.html
/usr/share/gtk-doc/html/amtk-5/api-index-3-0.html
/usr/share/gtk-doc/html/amtk-5/api-index-4-0.html
/usr/share/gtk-doc/html/amtk-5/api-index-5-0.html
/usr/share/gtk-doc/html/amtk-5/api-index-full.html
/usr/share/gtk-doc/html/amtk-5/api-reference.html
/usr/share/gtk-doc/html/amtk-5/gradual-porting.html
/usr/share/gtk-doc/html/amtk-5/home.png
/usr/share/gtk-doc/html/amtk-5/index.html
/usr/share/gtk-doc/html/amtk-5/left-insensitive.png
/usr/share/gtk-doc/html/amtk-5/left.png
/usr/share/gtk-doc/html/amtk-5/object-tree.html
/usr/share/gtk-doc/html/amtk-5/right-insensitive.png
/usr/share/gtk-doc/html/amtk-5/right.png
/usr/share/gtk-doc/html/amtk-5/style.css
/usr/share/gtk-doc/html/amtk-5/up-insensitive.png
/usr/share/gtk-doc/html/amtk-5/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libamtk-5.so.0
/usr/lib64/libamtk-5.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/amtk/757b86330df80f81143d5916b3e92b4bcb1b1890

%files locales -f amtk-5.lang
%defattr(-,root,root,-)


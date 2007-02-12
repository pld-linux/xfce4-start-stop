Summary:	Starts or stops Xfce4 components
Summary(pl.UTF-8):   Włączanie lub wyłączanie komponentów Xfce4
Name:		xfce4-start-stop
Version:	0.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.loculus.nl/xfce/files/%{name}-%{version}.tar.gz
# Source0-md5:	1e07ee87d70a1c2792472fd8097a0666
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfcegui4-devel
BuildRequires:	pkgconfig
Requires:	libxfce4util
Requires:	libxfcegui4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce4-start-stop is a small tool which can start and stop several
Xfce4 components with just one mouse click.

%description -l pl.UTF-8
Xfce4-start-stop jest małym narzędziem pozwalającym na włączenie
lub wyłączenie poszczególnych komponentów Xfce pojedynczym
kliknięciem.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop

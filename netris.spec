Summary:	A free networked version of T*tris
Summary(pl.UTF-8):	Darmowa, sieciowa wersja T*trisa
Name:		netris
Version:	0.52
Release:	9
License:	GPL v2+
Group:		Applications/Games
Source0:	ftp://ftp.netris.org/pub/netris/%{name}-%{version}.tar.gz
# Source0-md5:	b55af5697175ee06f7c6e40101979c38
Patch0:		%{name}-make.patch
Patch1:		%{name}-debian.patch
Patch2:		%{name}-link.patch
URL:		http://www.netris.org/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free networked version of T*tris.

%description -l pl.UTF-8
Darmowa, sieciowa wersja T*trisa.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
./Configure \
	--cc "%{__cc}" \
	--copt "%{rpmcflags} %{rpmcppflags}" \
	--lextra "%{rpmldflags}"

%{__make} proto.h
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}

install {netris,sr} $RPM_BUILD_ROOT%{_bindir}
install debian/*.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ *_desc
%attr(755,root,root) %{_bindir}/netris
%attr(755,root,root) %{_bindir}/sr
%{_mandir}/man6/netris.6*
%{_mandir}/man6/netris-sample-robot.6*

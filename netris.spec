Summary:	A free networked version of T*tris
Summary(pl):	Darmowa, sieciowa wersja T*trisa
Name:		netris
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.netris.org/pub/netris/%{name}-%{version}.tar.gz
# Source0-md5:	a30c950fd4e4779a26f856bc7cd1aaff
Patch0:		%{name}-make.patch
URL:		http://www.netris.org/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free networked version of T*tris.

%description -l pl
Darmowa, sieciowa wersja T*trisa.

%prep
%setup -q
%patch0 -p1

%build
./Configure \
	--copt "%{rpmcflags}"
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install netris	$RPM_BUILD_ROOT%{_bindir}
install sr	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ *_desc
%attr(755,root,root) %{_bindir}/*

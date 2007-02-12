Summary:	A free networked version of T*tris
Summary(pl.UTF-8):   Darmowa, sieciowa wersja T*trisa
Name:		netris
Version:	0.52
Release:	4
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.netris.org/pub/netris/%{name}-%{version}.tar.gz
# Source0-md5:	b55af5697175ee06f7c6e40101979c38
Patch0:		%{name}-make.patch
Patch1:		%{name}-debian.patch
URL:		http://www.netris.org/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free networked version of T*tris.

%description -l pl.UTF-8
Darmowa, sieciowa wersja T*trisa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./Configure \
	--copt "%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install {netris,sr} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ *_desc
%attr(755,root,root) %{_bindir}/*

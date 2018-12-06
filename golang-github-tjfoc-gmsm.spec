# https://github.com/tjfoc/gmsm
%global goipath github.com/tjfoc/gmsm
%global tag     v1.1

Name:           golang-github-tjfoc-gmsm
Version:        1.1
Release:        4%{?dist}
Summary:        GM SM2/3/4 library based on Golang
License:        ASL 2.0

%gometa

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(golang.org/x/crypto/ripemd160)
BuildRequires:  golang(golang.org/x/crypto/sha3)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.1-4
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 26 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1-1
- Update to version 1.1.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1.20171023.git9d99fac
- First package for Fedora


%global packname  scatterplot3d
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          0.3.35
Release:          2
Summary:          3D Scatter Plot
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/scatterplot3d_0.3-35.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
%rename R-cran-scatterplot3d

%description
Plots a three dimensional (3D) point cloud.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/po


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3_33-1
+ Revision: 775060
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3_32-1
+ Revision: 774902
- Update and rebuild with R2spec
- Update and rebuild with R2spec

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.3.27-2mdv2010.0
+ Revision: 433150
- BR texinfo
- rebuild

* Wed Jun 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.27-1mdv2009.0
+ Revision: 228959
- add buildrequires on tetex-latex
- import R-cran-scatterplot3d




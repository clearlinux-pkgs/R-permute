#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-permute
Version  : 0.9.4
Release  : 9
URL      : https://cran.r-project.org/src/contrib/permute_0.9-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/permute_0.9-4.tar.gz
Summary  : Functions for Generating Restricted Permutations of Data
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
## Restricted permutations with R
#### Released version
[![CRAN version](http://www.r-pkg.org/badges/version/permute)](https://cran.r-project.org/package=permute) [![](http://cranlogs.r-pkg.org/badges/grand-total/permute)](https://cran.r-project.org/package=permute)

%prep
%setup -q -c -n permute

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521196094

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521196094
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library permute
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library permute
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library permute
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library permute|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/permute/COPYRIGHTS
/usr/lib64/R/library/permute/ChangeLog
/usr/lib64/R/library/permute/DESCRIPTION
/usr/lib64/R/library/permute/INDEX
/usr/lib64/R/library/permute/Meta/Rd.rds
/usr/lib64/R/library/permute/Meta/data.rds
/usr/lib64/R/library/permute/Meta/features.rds
/usr/lib64/R/library/permute/Meta/hsearch.rds
/usr/lib64/R/library/permute/Meta/links.rds
/usr/lib64/R/library/permute/Meta/nsInfo.rds
/usr/lib64/R/library/permute/Meta/package.rds
/usr/lib64/R/library/permute/Meta/vignette.rds
/usr/lib64/R/library/permute/NAMESPACE
/usr/lib64/R/library/permute/NEWS
/usr/lib64/R/library/permute/R/permute
/usr/lib64/R/library/permute/R/permute.rdb
/usr/lib64/R/library/permute/R/permute.rdx
/usr/lib64/R/library/permute/TODO.md
/usr/lib64/R/library/permute/data/jackal.rda
/usr/lib64/R/library/permute/doc/index.html
/usr/lib64/R/library/permute/doc/permutations.R
/usr/lib64/R/library/permute/doc/permutations.Rnw
/usr/lib64/R/library/permute/doc/permutations.pdf
/usr/lib64/R/library/permute/help/AnIndex
/usr/lib64/R/library/permute/help/aliases.rds
/usr/lib64/R/library/permute/help/paths.rds
/usr/lib64/R/library/permute/help/permute.rdb
/usr/lib64/R/library/permute/help/permute.rdx
/usr/lib64/R/library/permute/html/00Index.html
/usr/lib64/R/library/permute/html/R.css

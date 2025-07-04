#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v27
# autospec commit: 65cf152
#
Name     : R-permute
Version  : 0.9.8
Release  : 51
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/permute_0.9-8.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/permute_0.9-8.tar.gz
Summary  : Functions for Generating Restricted Permutations of Data
Group    : Development/Tools
License  : GPL-2.0
Requires: R-permute-license = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
## Restricted permutations with R
[![CRAN version](https://www.r-pkg.org/badges/version/permute)](https://cran.r-project.org/package=permute)
[![](https://cranlogs.r-pkg.org/badges/grand-total/permute)](https://cran.r-project.org/package=permute)
[![R-CMD-check](https://github.com/gavinsimpson/permute/workflows/R-CMD-check/badge.svg)](https://github.com/gavinsimpson/cocorresp/actions)
[![codecov](https://codecov.io/gh/gavinsimpson/permute/graph/badge.svg?token=2FYEfBBSJ7)](https://app.codecov.io/gh/gavinsimpson/permute)

%package license
Summary: license components for the R-permute package.
Group: Default

%description license
license components for the R-permute package.


%prep
%setup -q -n permute
pushd ..
cp -a permute buildavx2
popd
pushd ..
cp -a permute buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1750884790

%install
export SOURCE_DATE_EPOCH=1750884790
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-permute
cp %{_builddir}/permute/inst/COPYRIGHTS %{buildroot}/usr/share/package-licenses/R-permute/42cb25c8687ae0504996af5c0f3e9139dbbb5a95 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/permute/doc/permutations.Rmd
/usr/lib64/R/library/permute/doc/permutations.html
/usr/lib64/R/library/permute/help/AnIndex
/usr/lib64/R/library/permute/help/aliases.rds
/usr/lib64/R/library/permute/help/paths.rds
/usr/lib64/R/library/permute/help/permute.rdb
/usr/lib64/R/library/permute/help/permute.rdx
/usr/lib64/R/library/permute/html/00Index.html
/usr/lib64/R/library/permute/html/R.css
/usr/lib64/R/library/permute/tests/Examples/permute-Ex.Rout.save
/usr/lib64/R/library/permute/tests/testthat.R
/usr/lib64/R/library/permute/tests/testthat/test-allPerms.R
/usr/lib64/R/library/permute/tests/testthat/test-as-methods.R
/usr/lib64/R/library/permute/tests/testthat/test-blocks.R
/usr/lib64/R/library/permute/tests/testthat/test-check.R
/usr/lib64/R/library/permute/tests/testthat/test-get-methods.R
/usr/lib64/R/library/permute/tests/testthat/test-how.R
/usr/lib64/R/library/permute/tests/testthat/test-nobs.R
/usr/lib64/R/library/permute/tests/testthat/test-numPerms.R
/usr/lib64/R/library/permute/tests/testthat/test-permute-fun.R
/usr/lib64/R/library/permute/tests/testthat/test-set-methods.R
/usr/lib64/R/library/permute/tests/testthat/test-shuffle-utils.R
/usr/lib64/R/library/permute/tests/testthat/test-shuffle.R
/usr/lib64/R/library/permute/tests/testthat/test-shuffleSet.R

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-permute/42cb25c8687ae0504996af5c0f3e9139dbbb5a95

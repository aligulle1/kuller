#!/bin/bash

# cd /var/tmp/pisi/linux-headers-2.6.15-2/work/
# cp linux-2.6.15/ linux-2.6.15.orig -pr
# fixHeaders.sh linux-2.6.15
# diff -ur linux-2.6.15.orig/include/ linux-2.6.15/include/ > linux-2.6.15-fixHeaders.patch

headers___fix() {
    # Voodoo to partially fix broken upstream headers.
    sed -i \
        -e "s/\([ "$'\t'"]\)\(u\|s\)\(8\|16\|32\|64\)\([ "$'\t'"]\)/\1__\2\3\4/g;" \
        -e 's/ \(u\|s\)\(8\|16\|32\|64\)$/ __\1\2/g' \
        -e 's/\([(, ]\)\(u\|s\)64\([, )]\)/\1__\264\3/g' \
        -e "s/^\(u\|s\)\(8\|16\|32\|64\)\([ "$'\t'"]\)/__\1\2\3/g;" \
        -e "s/ inline / __inline__ /g" \
        "$@"
}

cd "$1"/include

echo "Applying automated fixes:"
for i in asm-* linux
do
    cd $i
    headers___fix $(find . -mindepth 1 -type f -print)
    cd ..
done

echo "Done..."


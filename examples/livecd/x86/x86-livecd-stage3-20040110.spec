subarch: x86
version_stamp: 20040110
target: livecd-stage3
rel_type: default
rel_version: 1.4
snapshot: 20040110
source_subpath: default-x86-1.4/livecd-stage2-x86-20040110
boot/kernel: gentoo
livecd-stage3/cdtar: /var/home/drobbins/cvs/gentoo/src/catalyst/examples/livecd/cdtar/isolinux-2.08-cdtar.tar.bz2
livecd-stage3/runscript: /var/home/drobbins/cvs/gentoo/src/catalyst/examples/livecd/runscript/x86-isolinux-loop-example.sh
livecd-stage3/unmerge:
	autoconf automake bin86 binutils libtool m4 bison ld.so make perl patch linux-headers man-pages
	sash bison flex gettext texinfo ccache addpatches man groff lib-compat gcc python miscfiles ucl
livecd-stage3/empty:
	/var/tmp
	/var/cache
	/var/db
	/var/empty
	/var/cache
	/var/lock
	/tmp
	/usr/portage
	/usr/share/man
	/usr/share/info
	/usr/share/unimaps
	/usr/include
	/usr/share/zoneinfo
	/usr/share/dict
	/usr/share/doc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/lib/python2.2
	/usr/lib/portage
	/usr/share/gettext
	/usr/share/i18n
	/usr/share/rfc
	/usr/X11R6/man
	/usr/X11R6/include
	/usr/X11R6/lib/X11/config
	/usr/X11R6/lib/X11/etc
	/usr/X11R6/lib/X11/doc
	/usr/src
	/usr/share/doc
	/usr/share/man
livecd-stage3/rm:
	/lib/*.a
	/usr/lib/*.a
	/usr/lib/gcc-lib/*/*/libgcj*
	/usr/X11R6/lib/*.a

def get_mock_nvm_data():
    return b"*\x02" +\
        b"[$FIRSTPAGE      " +\
        b"*\x03" +\
        b"<_COPY   #\xff\x80\x00*\x02+\x45+\x44" +\
        b"<_PASTE  #\x00\xff\x00*\x02+\x45+\x47" +\
        b"<_CUT    #\x00\x00\xff*\x02+\x66+\x67" +\
        b"[$SECONdPAGE     " +\
        b"*\x04" +\
        b"<_FOO    #\xff\x80\x00*\x02+\x45+\x44" +\
        b"<_BAR    #\x00\xff\x00*\x02+\x45+\x47" +\
        b"<_BAZ    #\x00\x00\xff*\x02+\x66+\x67" +\
        b"<_BUZ    #\xff\x00\x00*\x03+\x66+\x67-\x67" +\
        b"\n\23\22\21\20\23\22\21\20\n\0\0\0\0\0\0"

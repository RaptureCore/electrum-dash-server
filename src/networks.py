# Main network and testnet3 definitions

# Rapture src/chainparams.cpp
params = {
    'rapture_main': {
        'pubkey_address': 60, #L120
        'script_address': 16, #L122
        'genesis_hash': '000007beab6b60ea39b8c553dcae06ffa5e4b57077df2c5ca1debe807e2d0017' #L110
    },
    'rapture_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000d504c2b5622c6c3a1c0c3321fe58b6c79a442f5e7143ee0c0e5903cda3f' #L210
    }
}

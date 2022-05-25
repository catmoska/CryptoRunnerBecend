import { Connection, actions, NodeWallet } from "@metaplex/js";
import { Keypair } from "@solana/web3.js";
// if (debug) NETWORK = clusterApiUrl("testnet");
// else NETWORK = clusterApiUrl("mainnet-beta");

export const run = async () => {
  i();
};

async function i() {
  const connection = new Connection("testnet");
  console.log("ddddf");

  var s = "Yypn5xvGcQNbge8ae1R4emHjQzrCgi8ZHfwGtG7pLPXTd847NR3qicsvMpvfuP8Mk2EPkwwpwUTHxYpSUf3SQ5C";
  var result = [];

  for (var i = 0; i < s.length; i += 2) {
    result.push(parseInt(s.substring(i, i + 2), 16));
  }
  let result2 = Uint8Array.from(result);
  console.log(result2);

  let secretKey: Uint8Array = Uint8Array.from([]);
  await actions.mintNFT({
    connection,
    uri: "https://www.arweave.net/1r-ImuiIxFl18UQolAoBnwLDMVcjkVAHruhtsaBpA7U?ext=json",
    wallet: new NodeWallet(Keypair.fromSecretKey(result2)),
  });
}


import { tranzacsion, getProvider, getProviderConect } from "./tranzact";
import { getData,log } from "./funcsionLogic";

Object.assign(window, {
  textMesends: textMesends,
  conect: conect,
  NFTnokunka: NFTnokunka,
  start: start,
  // url:url
});

let url: string = "";
let urlGeim: string = "";
let urlNFTbui: string = "";

function start(url1, url2, url3) {
  url = url1;
  urlGeim = url2;
  urlNFTbui = url3;
}

function textMesends(moneu, distansion) {
  return "fff" + moneu + " " + distansion;
}
////////

async function conect() {
  try {
    const provaider = await getProviderConect();
    const publicKey = provaider.publicKey.toString();
    await getData("POST", url, {
      publicKey: publicKey,
    });
    window.location.href = urlGeim;
  } catch (err) {
    window.open("https://phantom.app/", "_blank");
  }
}

async function NFTnokunka(i, y) {
  log(y);
  log(i);
  let signature = null;
  if (y == "bui") {
    document.getElementById("bloc1").style.display ='none';
    document.getElementById("bloc2").style.display ='';
    
    signature = await tranzacsion();
    log(signature)
    if (!signature["signature"]) {
      window.location.href = "";
      return;
    }
    document.getElementById("bloc1").style.display ='none';
    document.getElementById("bloc2").style.display ='none';
    document.getElementById("bloc3").style.display ='';
  
    await getData("POST", urlNFTbui, {
      NFT: i,
      onerasia: y,
      signatura: signature["signature"],
      conect:signature["NETWORK"],
    });
    return;
  }

  if (y == "sell") {
    let prises = await prompt("prais: snimaim 4%");
    prises = prises.replace( /,/g, "." )
    let prise2 = parseFloat(prises);
    log(prise2);
    log(isNaN(prise2))
    if(isNaN(prise2)){
      alert("nou number");
      return;
    }
    else if(prise2<0.00001){
      alert("malenkoe");
      return;
    }
    await getData("POST", urlNFTbui, {
      NFT: i,
      onerasia: y,
      prise:prise2
    });
    window.location.href = '';
    return;
  }

  await getData("POST", urlNFTbui, {
    NFT: i,
    onerasia: y,
  });
  window.location.href = '';
}

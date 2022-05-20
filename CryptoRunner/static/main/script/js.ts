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
    const buttonBui = document.getElementById("buttonBui");
    buttonBui.innerHTML = `<div class="text-center">не закриваите странису<div>
    <video autoplay muted loop preload="auto" class="width40">
    <source src='https://i.gifer.com/XOsX.mp4'>
    </video>`;

    signature = await tranzacsion();
    log(signature)
    if (!signature["signature"]) {
      window.location.href = "";
      return;
    }
    document.getElementById("bloc1").style.display ='none';
    document.getElementById("bloc2").style.display ='';
  
    await getData("POST", urlNFTbui, {
      NFT: i,
      onerasia: y,
      signatura: signature["signature"],
      conect:signature["NETWORK"],
    });
  }

  await getData("POST", urlNFTbui, {
    NFT: i,
    onerasia: y,
  });
}

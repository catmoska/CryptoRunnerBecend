// ???????? url ???? a
export function SmenaSilki(teg, A) {
  try {
    document.getElementById(teg).href = A;
    return true;
  } catch (err) {
    return false;
  }
}

// ???????? ?????????
export function SmenaBackground(A) {
  try {
    let f = document.getElementById("body").background;
    document.getElementById("body").background = A;
    return f;
  } catch (err) {
    return;
  }
}

// ??????? ? ????????? ? style.display (??????)
export async function displayStile(id,vklus,time=500){
  let i = "none"
  if (vklus) i="";
  return await setTimeout(() => (document.getElementById(id).style.display = i),time);
}
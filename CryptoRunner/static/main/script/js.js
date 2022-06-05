export function SmenaSilki(teg, A) {
  try {
    document.getElementById(teg).href = A;
    return true;
  } catch (err) {
    return false;
  }
}

export function SmenaBackground(A) {
  try {
    let f = document.getElementById("body").background;
    document.getElementById("body").background = A;
    // console.log(f);
    return f;
  } catch (err) {
    return;
  }
}

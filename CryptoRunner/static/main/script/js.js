export function SmenaSilki(teg,A){
    try{
        document.getElementById(teg).href = A;
        return true;
    }
    catch(err){
        return false; 
    }
}
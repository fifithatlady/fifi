(()=>{const e=document.querySelector("#signUpForm");e.addEventListener("submit",(async t=>{t.preventDefault();const r=new FormData(e);try{const e=await fetch("https://quicksearchestates.github.io/api/signup",{method:"POST",body:r});if(e.ok)window.location.href="https://quicksearchestates.github.io/dashboard";else{const t=await e.text();alert(t)}}catch(e){console.error("Error:",e),alert("An unexpected error occurred. Please try again later.")}}));const t=document.querySelector("#propertySearchForm");t.addEventListener("submit",(async e=>{e.preventDefault();const r=new FormData(t);try{const e=await fetch("https://quicksearchestates.github.io/api/properties/search",{method:"POST",body:r});if(e.ok)a=await e.json(),console.log(a);else{const t=await e.text();alert(t)}}catch(e){console.error("Error:",e),alert("An unexpected error occurred. Please try again later.")}var a}))})();
//# sourceMappingURL=bundle.js.map
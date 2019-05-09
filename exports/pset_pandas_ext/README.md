# [101 Pandas problems](https://www.machinelearningplus.com/python/101-pandas-exercises-python/)

Exported from link above

```js
Array.from(document.querySelectorAll('.collapseomatic_content')).forEach(k => k.style.display = 'block');
JSON.stringify(Array.from(document.querySelectorAll('h2[id*="howto"]')).map((curr, idx) => {
	let p1 = "";
	let p2 = "";
	let i = 0;

	while (curr.nextSibling && curr.nextSibling.tagName !== "H2") {
		console.log(idx, curr && curr.classList && curr.classList, curr && curr.classList && curr.tagName)
		if (curr.nodeType === Node.TEXT_NODE) {
			p1 += '"""\n' + curr.textContent + '\n"""\n';
        }
		else if (i === 0 || !curr.classList.contains('collapseomatic')) {
			
			if (curr.classList.contains('prettyprinted')) {
				
				p1 += '"""\n' + curr.querySelector('code').textContent + '\n"""\n';
            }
			else p1 += '"""\n' + curr.textContent + '\n"""\n';
        }
		else {
			
			p2 = p1 + '\n' + curr.nextSibling.querySelector('.prettyprinted code').textContent
        }
		i++;
		curr = curr.nextSibling;
    }
	return {p: p1, s: p2};
}))
```


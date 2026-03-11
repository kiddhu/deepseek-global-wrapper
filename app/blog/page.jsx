
import React, { useEffect, useState } from 'react';

export default function BlogPage() {
  const [content, setContent] = useState('Loading...');
  useEffect(() => {
    fetch('https://raw.githubusercontent.com/kiddhu/deepseek-global-wrapper/main/blog-post.md')
      .then(res => res.text()).then(text => setContent(text));
  }, []);
  return <div style={{padding: '50px', maxWidth: '800px', margin: '0 auto', fontFamily: 'sans-serif'}}>
    <a href="/">← Home</a>
    <pre style={{whiteSpace: 'pre-wrap', marginTop: '20px'}}>{content}</pre>
  </div>;
}

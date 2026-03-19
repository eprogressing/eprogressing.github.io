---
permalink: /cv/
title: "CV"
excerpt: "Online preview and download for my latest curriculum vitae."
author_profile: true
---

<div class="cv-page">
  <p class="cv-page__lead">
    This page hosts the latest version of my CV. If the embedded preview does not load in your browser, you can still open the PDF in a new tab or download it directly.
  </p>

  <div class="cv-actions">
    <a class="btn" href="{{ '/files/jingming-liang-cv.pdf' | relative_url }}" target="_blank" rel="noopener noreferrer">Open PDF</a>
    <a class="btn btn--inverse" href="{{ '/files/jingming-liang-cv.pdf' | relative_url }}" download>Download CV</a>
  </div>

  <div class="cv-embed">
    <iframe
      src="{{ '/files/jingming-liang-cv.pdf' | relative_url }}"
      title="Jingming Liang CV"
      loading="lazy">
    </iframe>
  </div>
</div>

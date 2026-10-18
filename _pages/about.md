---
permalink: /
title: ""
excerpt: ""
description: "Jingming Liang is a Computer Science undergraduate at Nankai University working on AI infrastructure, heterogeneous computing, and on-device AI."
author_profile: true
mathjax: false
redirect_from: 
  - /about/
  - /about.html
---

<div style="text-align: center; margin: 0 0 1.5rem 0;">
  <img
    src="{{ '/images/hero.svg' | relative_url }}"
    alt="Personal belief hero image"
    style="display: inline-block; width: 100%; max-width: 960px; height: auto;"
    loading="eager"
    fetchpriority="high"
    decoding="async"
  />
</div>

<span class='anchor' id='about-me'></span>

I'm **Jingming Liang** (Brighton), a senior undergraduate in Computer Science at [**Nankai University**](https://www.nankai.edu.cn/). Since **October 2025**, I have been an **undergraduate research intern** at the [**Nankai–Baidu Joint Laboratory (NBJL)**](https://nbjl.nankai.edu.cn/), and I expect to begin my PhD there in **2027**. Originally from Dalian, I also pursue minors in Finance and Criminal Law.

I build open-source tools and share learning resources through [**Lamplighter Commons**](https://github.com/lamplighter-commons), and contribute to [**StarryOS / tgoskits**](https://github.com/rcore-os/tgoskits) ([merged contributions](https://github.com/rcore-os/tgoskits/pulls?q=is%3Apr+author%3Aeprogressing+is%3Amerged)). For research and collaboration, reach me at [liangjm@nbjl.nankai.edu.cn](mailto:liangjm@nbjl.nankai.edu.cn).

**Research Interests:**

<ul class="research-interests-list">
  <li><strong>AI Infrastructure (AI Infra)</strong>: Scalable systems for AI training and inference, with a focus on distributed execution, communication, resource scheduling, and efficient model serving.</li>
  <li><strong>Heterogeneous Computing and GPU Optimization</strong>: Hardware-aware optimization across CPUs, GPUs, and NPUs, including efficient kernels and runtimes, with applications to on-device AI under memory and power constraints.</li>
  <li><strong>Embodied Intelligence and Systems Optimization</strong>: Efficient execution of perception and decision-making models, with an interest in deployment under real-time, memory, and compute constraints.</li>
</ul>

# 🔥 News
<ul class="news-list">
  <li class="news-list__item">
    <div class="news-list__meta"><strong class="news-list__date">[Oct 2026]</strong><span class="news-list__status">Open Source</span></div>
    <span class="news-list__title">Lamplighter Commons</span>
    <span class="news-list__body">I founded <a href="https://github.com/lamplighter-commons">Lamplighter Commons</a> to share open-source tools and learning resources.</span>
  </li>
  <li class="news-list__item">
    <div class="news-list__meta"><strong class="news-list__date">[Aug 2026]</strong><span class="news-list__status">Competitions</span></div>
    <span class="news-list__title">National awards in AI systems</span>
    <span class="news-list__body">Received national third prizes in the Xiandao Cup and Operating System Design Contest, plus Third Prize and the Special Contribution Award in the CANN-HCCL competition.</span>
  </li>
  <li class="news-list__item">
    <div class="news-list__meta"><strong class="news-list__date">[Sep 2025]</strong><span class="news-list__status">GPU Systems</span></div>
    <span class="news-list__title">CCF-TCARCH National Champion</span>
    <span class="news-list__body">Won the national championship as an individual competitor, working on GPU optimization for APSP, prefix sum, and softmax.</span>
  </li>
</ul>

# 📝 Projects and Research

## Selected Systems Projects

<div class='paper-box'><div class='paper-box-image'><div class="project-visual"><div class="badge">GPU Systems</div><div class="project-figure"><img src="{{ '/images/projects/optimized/apsp-gpu-optimization.webp' | relative_url }}" alt="APSP GPU optimization project overview" width="1000" height="563" style="width: 100%; height: auto;" loading="eager" decoding="async"></div></div></div>
<div class='paper-box-text' markdown="1">

**GPU Optimization for All-Pairs Shortest Path**

<p class="project-meta">Individual competition project · Aug–Sep 2025 · CCF-TCARCH National Champion</p>

- Designed a **memory-aware 3-stage blocked Floyd–Warshall pipeline** to reduce bandwidth pressure in dense APSP computation, using shared memory to improve data locality.
- Optimized kernel execution through fusion, dual-stream scheduling, double buffering, and reduced synchronization overhead. Further compressed **host-to-device transfer cost from O(V²) to O(E)** via custom I/O and device-side graph reconstruction.
- Ranked 1st nationally as an individual competitor, reducing end-to-end runtime by **52.9%** on the official hidden datasets (11.50s → 5.42s), equivalent to a **2.12× speedup** through profiling-driven optimization and systematic performance tuning.

</div>
</div>
<div class='paper-box'><div class='paper-box-image'><div class="project-visual"><div class="badge">On-Device AI</div><div class="project-figure"><a href="{{ '/images/projects/optimized/starryos-competition-ball-pickup.webp' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="Open the full competition photograph"><img class="project-photo" src="{{ '/images/projects/optimized/starryos-competition-ball-pickup.webp' | relative_url }}" alt="Our tennis-ball retrieval robot holding a ball on the actual operating-system competition floor, beside the collection bucket." width="1333" height="1000" style="width: 100%; height: auto;" loading="eager" decoding="async"></a></div></div></div>
<div class='paper-box-text' markdown="1">

**On-Device AIOS on RK3588 and StarryOS**

<p class="project-meta">Team competition project · May–Aug 2026 · Team captain; perception-to-control integration and OS performance optimization.</p>

- Integrated **UVC image acquisition, RKNN/NPU inference, object detection, and robotic-arm control** into a tennis-ball retrieval robot running on RK3588 and StarryOS.
- Diagnosed RKNPU execution and SMP scheduling, fixing hot-path logging stalls and tasks remaining on a single core. In the project measurements, **rknn_run latency fell from 817 to 211 ms**.
- Improved the **four-thread speedup from 0.96× to 3.45×** in the project tests; the team received a **National Third Prize** in the 2026 Operating System Design Contest.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="project-visual"><div class="badge">AI Infrastructure</div><div class="project-figure"><img src="{{ '/images/projects/optimized/xiandao-serving-concept-v3.webp' | relative_url }}" alt="Conceptual illustration of Qwen3.5-27B serving with vLLM, KV cache, and TP=2 across two DCU accelerators." width="1000" height="563" style="width: 100%; height: auto;" loading="eager" decoding="async"></div></div></div>
<div class='paper-box-text' markdown="1">

**LLM Inference Serving on Domestic DCUs**

<p class="project-meta">Individual competition project · Jul–Aug 2026 · Kernel and serving optimization.</p>

- Profiled **Qwen3.5-27B with vLLM** for long-context inference on domestic DCUs, separating prefill/decode bottlenecks and analyzing attention and paged KV-cache paths.
- Optimized compute and memory access with **FlashAttention, Triton GEMV, and CUDA Graph**, and adapted **TP=2 tensor parallelism and Custom AllReduce** for two-device serving.
- Completed optimization from individual kernels to the serving pipeline, placing **12th nationally** and receiving a **National Third Prize** in the 2026 Xiandao Cup.

</div>
</div>


## Research

<div class='paper-box'><div class='paper-box-image'><div class="project-visual"><div class="badge">Multimodal MoE</div><div class="project-figure"><a href="{{ '/files/cmrd-method-pipeline.pdf' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="Open the full-size CMRD method pipeline PDF"><img src="{{ '/images/projects/optimized/cmrd-method-pipeline.webp' | relative_url }}" alt="CMRD pipeline: controlled routing probes, same-question controls, and diagnosis-guided mitigation." width="1600" height="497" style="width: 100%; height: auto;" loading="eager" decoding="async"></a></div></div></div>
<div class='paper-box-text' markdown="1">

**Diagnosing and Mitigating Noun-Driven Routing Bias in Multimodal Mixture-of-Experts**

<p class="project-meta">Research project · Routing probe design and experimental evaluation.</p>

- Developed **CMRD (Controlled MoE Routing Decomposition)**, a training-free probe using text anchors and controlled pre-router interventions to examine noun-driven visual routing shifts.
- Used **same-question controls** to approximately separate broad-semantic effects from a queried-specific residual, identifying a shared **layer-10 routing hotspot** in MoE-LLaVA-Qwen.
- Evaluated **Noun-Blind Routing** and **Two-Stage Verification** for object-existence hallucination. On **POPE-9000**, Two-Stage Verification reduced false positives by **about 60%** and improved accuracy from **81.7% to 88.2%**, while increasing false negatives.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="project-visual"><div class="badge">Diffusion Models</div><div class="project-figure"><img src="{{ '/images/projects/optimized/k-lora-overview-v2.webp' | relative_url }}" alt="K-LoRA project overview" width="1000" height="563" style="width: 100%; height: auto;" loading="eager" decoding="async"></div><p class="project-figure-note">Original K-LoRA: Ouyang et al., CVPR 2025. This overview provides background for the K-LoRA++ competition extension.</p></div></div>
<div class='paper-box-text' markdown="1">

**Adaptive Weight Scheduling for Image Diffusion Models (K-LoRA++)**

<p class="project-meta">Competition research project · Apr–Oct 2025 · Schedule formulation, evaluation, and demo development; National Third Prize in Challenge Cup.</p>

- Extended the original K-LoRA framework for training-free subject/style LoRA fusion by mathematically formulating and evaluating **8 distinct stage-aware scaling schedules** across diffusion timesteps.
- Compared the schedules through first-order derivative analysis and cross-domain experiments; a **constant-derivative linear schedule** gave the best content/style balance among the evaluated schedules in the tested settings, with less structural distortion and visual jitter.
- Facilitated the end-to-end development of the project's interactive demo and drove its practical deployment for downstream generative applications.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="project-visual"><div class="badge">LTSF</div><div class="project-figure"><img src="{{ '/images/projects/optimized/sparsetsf-fft.webp' | relative_url }}" alt="SparseTSF-FFT framework overview" width="1600" height="900" style="width: 100%; height: auto;" loading="eager" decoding="async"></div></div></div>
<div class='paper-box-text' markdown="1">

**SparseTSF-FFT: A Frequency-Domain Framework for Time Series Forecasting**

<p class="project-meta">Course project · Sep–Dec 2024 · Framework migration and model extension.</p>

- **Reimplemented and extended SparseTSF from PyTorch to MindSpore**, including custom API mappings and reconstruction of the training/evaluation pipeline for cross-framework deployment.
- Designed an **FFT-based learnable filtering module** to replace local sliding-window convolutions, aiming to better capture long-range periodic structure under a lightweight parameter budget.
- Conducted cross-framework profiling and forecasting evaluations, observing **improved long-horizon performance** (e.g., at 336 and 720 steps on ETTh1/ETTh2) relative to the baseline in the evaluated settings.

</div>
</div>

## Other Engineering Projects

<div class='paper-box'><div class='paper-box-image'><div class="project-visual"><div class="badge">Information Systems</div><div class="project-figure"><img src="{{ '/images/projects/optimized/raceradar-overview.webp' | relative_url }}" alt="RaceRadar iOS app overview" width="1000" height="563" style="width: 100%; height: auto;" loading="eager" decoding="async"></div></div></div>
<div class='paper-box-text' markdown="1">

**RaceRadar: An End-to-End iOS System for Aggregating and Prioritizing Competition Opportunities**

<p class="project-meta">Independent engineering project · Nov 2025–present · App Store release in preparation</p>

- Built a **fault-tolerant, multi-source ingestion pipeline** that continuously crawls, cleans, deduplicates, and ranks competition announcements, publishing a unified JSON feed through scheduled GitHub Actions workflows.
- Developed a **native iOS app in Swift/Xcode** with card-based discovery, detailed opportunity pages, deadline-aware prioritization, source/category tagging, and shareable competition posters.
- Designed the system around real student workflows, translating automated data ingestion and ranking into a **deployable user-facing information system** for discovering higher-quality and time-sensitive opportunities.
</div>
</div>

{% include github-project-cards.html %}

# 🎖 Honors and Awards
<div class="award-board">
  <div class="award-board__intro">
    <p class="award-board__eyebrow">🏆 Competition Awards</p>
  </div>

  <section class="award-year-section">
    <div class="award-year-section__header"><h4 class="award-year-section__title">2026</h4><p class="award-year-section__meta">3 awards</p></div>
    <div class="award-grid">
      <article class="award-card">
        <div class="award-card__top"><span class="award-card__date">2026</span><span class="award-card__result">National Third Prize</span></div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://cc.nankai.edu.cn/2026/0909/c13295a602199/page.htm" target="_blank" rel="noopener noreferrer">Computer System Development Capability Competition — Operating System Design Contest (OS Function Challenge Track)</a></h5>
        <div class="award-card__tags"><span class="award-card__tag">Team captain</span><span class="award-card__tag award-card__tag--money">Prize ¥2,000</span></div>
      </article>
      <article class="award-card">
        <div class="award-card__top"><span class="award-card__date">2026</span><span class="award-card__result">National Third Prize</span></div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://cc.nankai.edu.cn/2026/0909/c13295a602200/page.htm" target="_blank" rel="noopener noreferrer">Computer System Development Capability Competition — Intelligent Computing Innovation Design Contest (Xiandao Cup)</a></h5>
        <div class="award-card__tags"><span class="award-card__tag">Solo entry</span><span class="award-card__tag award-card__tag--money">Prize ¥8,000</span></div>
      </article>
      <article class="award-card">
        <div class="award-card__top"><span class="award-card__date">2026</span><span class="award-card__result">Third Prize &amp; Special Contribution Award</span></div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://competition.gitcode.com/competition/2071411775170351105/winner-list" target="_blank" rel="noopener noreferrer">CANN-HCCL Communication Library Innovation Competition</a></h5>
        <div class="award-card__tags"><span class="award-card__tag">Solo entry</span><span class="award-card__tag award-card__tag--money">Prize ¥5,000 + ¥1,000</span></div>
      </article>
    </div>
  </section>

  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2025</h4>
      <p class="award-year-section__meta">12 awards</p>
    </div>
    <div class="award-grid">
      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.12</span>
          <span class="award-card__result">Second Place</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://forum.trae.cn/t/topic/213" target="_blank" rel="noopener noreferrer">TRAE on Campus Vibe Coding Workshop</a></h5>
        <div class="award-card__tags">
          <span class="award-card__tag">Solo entry</span>
          <span class="award-card__tag award-card__tag--money">Prize ¥1,500</span>
        </div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.12</span>
          <span class="award-card__result">Bronze Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://news.nankai.edu.cn/zhxw/system/2025/12/08/030070061.shtml" target="_blank" rel="noopener noreferrer">3rd National College Student Career Planning Competition - Growth Track, University-level Competition</a></h5>
      </article>

      <article class="award-card award-card--featured">
        <span class="award-card__spotlight">Featured Award</span>
        <div class="award-card__top">
          <span class="award-card__date">2025.11</span>
          <span class="award-card__result">National Third Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://www.jiemian.com/article/13643188.html" target="_blank" rel="noopener noreferrer">Computer System Development Capability Competition — Intelligent Computing Innovation Design Contest (Xiandao Cup)</a></h5>
        <div class="award-card__tags">
          <span class="award-card__tag award-card__tag--money">Prize ¥10,000</span>
        </div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.11</span>
          <span class="award-card__result">Provincial First Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://www.cmathc.org.cn/mcm/news/362.html" target="_blank" rel="noopener noreferrer">China Undergraduate Mathematical Contest in Modeling (CUMCM)</a></h5>
      <div class="award-card__tags"><span class="award-card__tag">Team captain</span></div>
      </article>

      <article class="award-card award-card--featured">
        <span class="award-card__spotlight">Featured Award</span>
        <div class="award-card__top">
          <span class="award-card__date">2025.10</span>
          <span class="award-card__result">National Third Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://news.nankai.edu.cn/ywsd/system/2025/11/10/030069539.shtml" target="_blank" rel="noopener noreferrer">19th Challenge Cup National Undergraduate Extracurricular Academic Science and Technology Works Competition</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.10</span>
          <span class="award-card__result">Silver Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://mp.weixin.qq.com/s/bO7zPc8JcLDxAw58Q5PqqQ" target="_blank" rel="noopener noreferrer">Nankai University Mathematical Modeling Competition</a></h5>
      </article>

      <article class="award-card award-card--flagship">
        <span class="award-card__spotlight">Flagship Award</span>
        <div class="award-card__top">
          <span class="award-card__date">2025.09</span>
          <span class="award-card__result">National Champion</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://cc-backend.nankai.edu.cn/news/news-detail/20808" target="_blank" rel="noopener noreferrer">8th CCF-TCARCH Computer Architecture Challenge</a></h5>
        <div class="award-card__tags">
          <span class="award-card__tag">Solo entry</span>
          <span class="award-card__tag award-card__tag--money">Prize ¥10,000</span>
        </div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.09</span>
          <span class="award-card__result">Special Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://mp.weixin.qq.com/s/npz3o1DdSBSMQ_omhiGmcw" target="_blank" rel="noopener noreferrer">Pioneer Cup Intelligent Computing Design Competition</a></h5>
        <div class="award-card__tags">
          <span class="award-card__tag award-card__tag--money">Prize ¥1,000</span>
        </div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.07</span>
          <span class="award-card__result">Grand Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://2025.tiaozhanbei.net/d49/article/666/" target="_blank" rel="noopener noreferrer">Challenge Cup Tianjin Undergraduate Extracurricular Academic Science and Technology Works Competition</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.06</span>
          <span class="award-card__result">Outstanding Award</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://nktw.nankai.edu.cn/info/1013/1910.htm" target="_blank" rel="noopener noreferrer">President's Cup Innovation and Entrepreneurship Competition - Entrepreneurship Track</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.04</span>
          <span class="award-card__result">First Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://nktw.nankai.edu.cn/info/1013/1879.htm" target="_blank" rel="noopener noreferrer">President's Cup Innovation and Entrepreneurship Competition - Innovation Track</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.01</span>
          <span class="award-card__result">Honorable Mention, H Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://www.comap.com/contests/mcm-icm" target="_blank" rel="noopener noreferrer">Mathematical Contest in Modeling / Interdisciplinary Contest in Modeling (MCM/ICM)</a></h5>
      <div class="award-card__tags"><span class="award-card__tag">Team captain</span></div>
      </article>
    </div>
  </section>

  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2024</h4>
      <p class="award-year-section__meta">2 awards</p>
    </div>
    <div class="award-grid">
      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2024.11</span>
          <span class="award-card__result">Provincial Second Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://jw.tjut.edu.cn/info/1888/6440.htm" target="_blank" rel="noopener noreferrer">China Undergraduate Mathematical Contest in Modeling (CUMCM)</a></h5>
      <div class="award-card__tags"><span class="award-card__tag">Team captain</span></div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2024.10</span>
          <span class="award-card__result">National First Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://zhuanlan.zhihu.com/p/10010914554" target="_blank" rel="noopener noreferrer">3rd National College Student Data Analysis Popular Science Competition</a></h5>
      <div class="award-card__tags"><span class="award-card__tag">Solo entry</span></div>
      </article>
    </div>
  </section>

</div>

<div class="service-board">
  <div class="service-board__intro">
    <p class="service-board__eyebrow">Teaching, Leadership, and Service</p>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Roles</p>
    <div class="service-list">
      <article class="service-item">
        <span class="service-item__date">Sep 2025 - Jan 2026</span>
        <div class="service-item__body">
          <p class="service-item__title">Teaching Assistant</p>
          <p class="service-item__meta">Computer Hardware Fundamentals</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">Sep 2025 - Jan 2026</span>
        <div class="service-item__body">
          <p class="service-item__title">Student Assistant</p>
          <p class="service-item__meta">Youth League Committee Office</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">Sep 2023 - Present</span>
        <div class="service-item__body">
          <p class="service-item__title">Class Monitor &amp; Youth League Branch Deputy Secretary</p>
          <p class="service-item__meta">School of Computer Science</p>
        </div>
      </article>
    </div>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Service Impact</p>
    <div class="service-stat-strip">
      <span class="service-chip"><strong>249.9h</strong> Volunteer Service</span>
      <span class="service-chip"><strong>153h</strong> Social Practice</span>
      <span class="service-chip"><strong>530h</strong> Peer Learning Support</span>
      <span class="service-chip"><strong>TEDx</strong> Official Volunteer</span>
    </div>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Selected Honors</p>
    <div class="service-honor-grid">
      <article class="service-item">
        <span class="service-item__date">2026</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Communist Youth League Member</p>
          <p class="service-item__meta">Nankai University May Fourth Honors</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2024, 2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Student Cadre</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Team</p>
          <p class="service-item__meta">Nankai Xiong'an Summer Social Practice</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Individual</p>
          <p class="service-item__meta">Teachers and Students Together in Four Aspects Social Practice</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Leader of the May Fourth Red Flag Youth League Group</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Class Youth League Branch</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2023</span>
        <div class="service-item__body">
          <p class="service-item__title">Official Representative</p>
          <p class="service-item__meta">Nankai University Student Congress</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2024</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Officer</p>
          <p class="service-item__meta">Organization Department, Youth League Committee</p>
        </div>
      </article>
    </div>
  </div>

</div>

# 🏅 Scholarships
<div class="award-board scholarship-board">
  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2026</h4>
      <p class="award-year-section__meta">1 scholarship</p>
    </div>
    <div class="award-grid">
      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2026.10</span>
          <span class="award-card__result scholarship-card__amount">CNY 5,000</span>
        </div>
        <h5 class="award-card__name">Gongneng Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>
    </div>
  </section>

  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2025</h4>
      <p class="award-year-section__meta">2 scholarships</p>
    </div>
    <div class="award-grid">
      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.11</span>
          <span class="award-card__result scholarship-card__amount">CNY 2,000</span>
        </div>
        <h5 class="award-card__name">Academic Progress Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>

      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.11</span>
          <span class="award-card__result scholarship-card__amount">CNY 2,000</span>
        </div>
        <h5 class="award-card__name">Student Service Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>
    </div>
  </section>

  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2024</h4>
      <p class="award-year-section__meta">2 scholarships</p>
    </div>
    <div class="award-grid">
      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2024.11</span>
          <span class="award-card__result scholarship-card__amount">CNY 2,000</span>
        </div>
        <h5 class="award-card__name">Social Welfare Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>

      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2024.11</span>
          <span class="award-card__result scholarship-card__amount">CNY 2,000</span>
        </div>
        <h5 class="award-card__name">Student Service Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>
    </div>
  </section>
</div>

<span class='anchor' id='-educations'></span>

# 📖 Education
<div class="education-card">
  <div class="education-card__header">
    <div class="education-card__main">
      <h3 class="education-card__school">Nankai University, School of Computer Science</h3>
      <p class="education-card__meta">Sep 2023 - Jun 2027 (Expected)</p>
      <div class="education-card__details">
        <p class="education-card__degree">B.Eng. Candidate in Computer Science and Technology</p>
        <p class="education-card__minor">Minors: Finance, Criminal Law.</p>
      </div>
    </div>
    <div class="education-card__side">
      <div class="education-card__tags">
        <span class="education-tag education-tag--strong">985 Project</span>
        <span class="education-tag education-tag--strong">211 Project</span>
        <span class="education-tag education-tag--soft">Double First-Class</span>
      </div>
      <img src="{{ '/images/nankai-emblem.png' | relative_url }}" alt="Nankai University emblem" class="education-card__emblem" loading="eager" decoding="async" />
    </div>
  </div>
</div>

<div class="education-card education-card--um">
  <div class="education-card__header">
    <div class="education-card__main">
      <h3 class="education-card__school">University of Macau, Faculty of Science and Technology</h3>
      <p class="education-card__meta">Exchange Programme Admission</p>
      <div class="education-card__details">
        <p class="education-card__degree">Admitted to the exchange programme in Computer and Information Science</p>
      </div>
    </div>
    <div class="education-card__side">
      <div class="education-card__tags">
        <span class="education-tag education-tag--strong">Admission offer</span>
        <span class="education-tag education-tag--soft">International Exchange</span>
        <span class="education-tag education-tag--soft">Macau SAR</span>
      </div>
      <img src="{{ '/images/optimized/um-emblem.webp' | relative_url }}" alt="University of Macau emblem" class="education-card__emblem" loading="eager" decoding="async" />
    </div>
  </div>
</div>

# 💼 Internships
<div class="internship-list">
  <article class="internship-card internship-card--featured internship-card--theme-unigrow">
    <div class="internship-card__header">
      <img src="{{ '/images/internships/optimized/unigrow-logo-horizontal-v2.svg' | relative_url }}" alt="UniGrow logo" class="internship-card__logo" loading="eager" decoding="async" />
      <div class="internship-card__header-main">
        <h3 class="internship-card__company">UniGrow, Technical Development</h3>
        <p class="internship-card__meta">Jun 2026 - Oct 2026</p>
      </div>
      <div class="internship-card__tags">
        <span class="internship-tag internship-tag--highlight">AI Agent Full-Stack Engineer Intern</span>
      </div>
    </div>
    <ul class="internship-card__highlights">
      <li><strong>Contributed to UniGrow from initial development to production delivery</strong>, working across AI agents, retrieval-augmented generation (RAG), mobile applications, and backend services.</li>
      <li><strong>Developed features and integrated systems</strong>, and handled CI/CD, server deployment, and Android/iOS release and maintenance.</li>
      <li><strong>Helped launch a product that reached 1,000+ registered users within two weeks</strong> of going live.</li>
    </ul>
  </article>

  <article class="internship-card internship-card--featured internship-card--theme-hejun">
    <div class="internship-card__header">
      <img src="{{ '/images/internships/optimized/hejun-logo.webp' | relative_url }}" alt="Hejun Consulting logo" class="internship-card__logo" loading="eager" decoding="async" />
      <div class="internship-card__header-main">
        <h3 class="internship-card__company">Hejun Consulting</h3>
        <p class="internship-card__meta">Jul 2025 - Sep 2025</p>
      </div>
      <div class="internship-card__tags">
        <span class="internship-tag internship-tag--highlight">Business Analysis Intern</span>
      </div>
    </div>
    <ul class="internship-card__highlights">
      <li><strong>Analyzed financial data from 2016–2024</strong> and recent water-utility market data from Beijing, Tianjin, and Hebei to support industry research.</li>
      <li><strong>Built market-size estimates, competitor comparisons, and regional-attractiveness indicators</strong> for equipment and chemical-supply market analysis.</li>
      <li><strong>Prepared a 30,000+ word industry report</strong> on the water-treatment equipment and chemicals sector.</li>
    </ul>
  </article>

  <article class="internship-card internship-card--featured internship-card--theme-chinasoft">
    <div class="internship-card__header">
      <img src="{{ '/images/internships/optimized/chinasoft-logo.webp' | relative_url }}" alt="ChinaSoft International logo" class="internship-card__logo" loading="eager" decoding="async" />
      <div class="internship-card__header-main">
        <h3 class="internship-card__company">ChinaSoft International, LLM Team</h3>
        <p class="internship-card__meta">Jun 2025 - Jul 2025</p>
      </div>
      <div class="internship-card__tags">
        <span class="internship-tag internship-tag--highlight">LLM Development Intern</span>
      </div>
    </div>
    <ul class="internship-card__highlights">
      <li><strong>Built an e-commerce knowledge base and RAG workflow</strong>, including data collection, structured extraction, knowledge-graph and vector-store integration, and retrieval tuning.</li>
      <li><strong>Fine-tuned a Qwen-based digital persona</strong> with supervised fine-tuning and 4-bit QLoRA on an RTX 4060 with 8 GB of memory.</li>
      <li><strong>Deployed the assistant through QQ</strong>, connecting model adaptation and retrieval to a working conversational application.</li>
    </ul>
  </article>

  <article class="internship-card internship-card--featured internship-card--theme-gtja">
    <div class="internship-card__header">
      <img src="{{ '/images/internships/optimized/gtja-logo.webp' | relative_url }}" alt="Guotai Junan Securities logo" class="internship-card__logo" loading="eager" decoding="async" />
      <div class="internship-card__header-main">
        <h3 class="internship-card__company">Guotai Junan Securities, Wealth Management</h3>
        <p class="internship-card__meta">Jun 2024 - Jul 2024</p>
      </div>
      <div class="internship-card__tags">
        <span class="internship-tag internship-tag--highlight">Quantitative Research Assistant</span>
      </div>
    </div>
    <ul class="internship-card__highlights">
      <li><strong>Cleaned nearly ten years of data across ten asset classes</strong> and calculated returns, volatility, and covariance matrices for portfolio analysis.</li>
      <li><strong>Implemented Markowitz mean–variance portfolio optimization</strong> to estimate the efficient frontier and a maximum-Sharpe portfolio.</li>
      <li><strong>Examined overfitting in corner solutions</strong> and explored adjustments using more recent time-series data.</li>
    </ul>
  </article>
</div>

<span class='anchor' id='technical-communication'></span>

# 📡 Technical Communication
<div class="news-board">
  <div class="news-board__header">
    <p class="news-board__eyebrow">Public Engagement</p>
    <p class="news-board__intro">I share computer science study notes and learning resources on Rednote, making course material accessible to a wider student audience.</p>
  </div>

  <div class="news-board__content">
    <article class="news-feature">
      <h4 class="news-feature__headline">CS and AI Educational Outreach</h4>
      <p class="news-feature__foot">Account statistics as of October 2026.</p>
      <div class="news-feature__stats">
        <span class="news-stat"><strong>6,211</strong> followers</span>
        <span class="news-stat"><strong>3M+</strong> total views</span>
        <span class="news-stat"><strong>156k</strong> likes and saves</span>
      </div>
    </article>

    <section class="news-gallery" aria-label="Snapshots of public-facing educational content">
      <div class="news-gallery__head">
        <span class="news-gallery__label">Visual Highlights</span>
        <p class="news-gallery__caption">Selected examples of educational content</p>
      </div>
      <div class="news-gallery__grid">
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/optimized/xiaohongshu-post-2.webp' | relative_url }}" alt="Xiaohongshu educational post screenshot 2" loading="eager" decoding="async">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/optimized/xiaohongshu-post-3.webp' | relative_url }}" alt="Xiaohongshu educational post screenshot 3" loading="eager" decoding="async">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/optimized/xiaohongshu-post-4.webp' | relative_url }}" alt="Xiaohongshu educational post screenshot 4" loading="eager" decoding="async">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/optimized/xiaohongshu-post-6.webp' | relative_url }}" alt="Xiaohongshu educational post screenshot 6" loading="eager" decoding="async">
        </figure>
      </div>
    </section>

    <article class="news-feature">
      <h4 class="news-feature__headline">Beyond Research</h4>
      <p class="news-feature__body">Outside computing, I play the violin and classical guitar (Grade 10 in both), and enjoy volleyball, marathon running, and independent travel.</p>
      <a class="news-feature__media" href="{{ '/images/20260303-143751.jpeg' | relative_url }}" target="_blank" rel="noopener noreferrer" aria-label="Open running photo">
        <img class="news-feature__photo" src="{{ '/images/athletics/optimized/running-moment-2.webp' | relative_url }}" alt="Running moment" loading="eager" decoding="async">
      </a>
    </article>
  </div>
</div>

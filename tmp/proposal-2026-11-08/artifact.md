# DOCX authoring contract

Reference: C:/ssafy/hyundaiUX/review/2026-11-06/root-6.docx
SHA256: 07BE893D58B0E96AB7788F0D189D6829F0E59A2CEE4BC18CB90EC37EEDA2F5FD
Reference is immutable. Word read-only export observed 5 pages. Template page 2 was rendered and visually inspected.

User-authorized scope: create a readable proposal containing only the official 02 section items 1 through 6. Keep their order and semantic headings. Do not fill participant data, consent, signatures, optional item 7 or item 8. This is an independent 02 excerpt based on a working copy of the reference, not a claim that the full application has been submitted.

Page geometry derives from reference: one A4 portrait section, w=7560310 EMU h=10692130 EMU, top=593725 bottom=575945 left=647700 right=647700. Preserve these dimensions. Reference Normal10pt, Title26pt, Heading1 14pt, Heading2 13pt. User requests polished readability: use Noto Sans KR10.5pt, line1.23, 6pt after; Title26pt; H1 15pt/H2 12.5pt, black. Preserve a coherent six-section hierarchy. No decorative rules, colored headings, boxed prose, or shaded callout cards. Tables are comparison/requirements/numeric matrices only, with D9D9D9 borders, pale blue header and alternating white/pale gray bodies.

Intentional scope/format deviations: remove original body outside 02 and the blank placeholder controls from the working copy; supply substantive rich content and embedded figures rather than retain empty four-line frames. Retain source styles as a starting point and override only relevant document roles. Replace source legal footer with a neutral proposal title and automatic page field, remove source personal metadata. Do not alter retained source.

Slots: 1 one-line summary and scope; 2 evidence and 8-service benchmark; 3 core functionality, vehicle rationale, form fields and anonymity boundary; 4 two fictional personas, platform reference and complete image journey with voice-only/optional meetup/exception branches; 5 verified SDK mapping, realistic pre-PT development plan, deployment and acceptance; 6 value, explicit scenario MAU/retention model, roadmap, actual research questionnaire, unofficial score, and cited source list. Sources stay inside six requested items.

Visual assets: 26 native-code UI state images plus full-tablet and app-window crops; two imagegen fictional persona photos; official platform reference where downloadable; proposed architecture and portrait responsive mockup. UI images are mock data and not evidence of running APK/SDK integration. Keep all source PNGs and a manifest in final assets ZIP. Do not imply live hardware, real survey responses, or verified retention.

Verification: source SHA256 unchanged; DOCX has exactly six first-level content headings; hyperlinks/citations resolve to listed URLs; 26 UI states cover form to voice-only and meetup endings plus trip termination and failures; all forecast values recomputed; Word export final DOCX to PDF in read-only mode, rasterize all pages with bundled Poppler and inspect all PNGs; independent source/privacy/SDK review and visual review, then iterate. Canonical render_docx.py was attempted and failed because LibreOffice is absent; installed Word hidden COM export is the observed successful native fallback. PDF and page PNGs are QA artifacts, not requested final deliverables.

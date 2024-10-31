# goebel-seq: Codes and computational results regarding $(k, l)$-Göbel sequences

Codes and data in this repository accompany the manuscript "A note on non-integrality of the $(k,l)$-Göbel sequences" \[[arXiv:2410.23240](https://arxiv.org/abs/2410.23240)\].

## Computational Results
Data files were created by merging the results from the computations based on the actual codes and removing overheads. These files, placed on the uppermost directory of the repository, are intended for circulation among the research community.
- `k-goebel_1e7.zip`: Computed values of $N_k$ for $k$ up to 10<sup>7</sup>. Compressed file in CSV format with entries separated by a comma and without a header line. The first and second rows represent $k$ and $N_k$, respectively.
- `k-goebel_sieve-mod_3e4.zip`: List of residue classes modulo $(p-1)$ for prime $p$, up to 30000, to be sieved out (i.e., $N_k \leq p$). Compressed file in CSV format with entries separated by a comma and without a header line. The first, second, and third rows represent prime $p$, the modulus, and the representative of the residue class, respectively.
- `k-goebel_sieve_cuda_15e3.txt`: List of integers greater than 1 up to 10<sup>14</sup> that were not sieved out by the residue classes modulo $(p-1)$ for prime $p < 15000$ listed in `k-goebel_sieve-mod_3e4.zip`. File in plain text format, where each line represents one entry.
- `k-l-goebel-mid_prime-integrality_1e6.csv`: Computed values of $l_\mathrm{L}$, $l_\mathrm{R}$, and $\\# J_p$ for prime $p \equiv 1 \pmod{4}$ with $13 \leq p \leq 10^6$. File in CSV format with entries separated by a comma and without a header line. The first, second, third, and forth rows represent prime $p$, $l_\mathrm{L}$, $l_\mathrm{R}$, and $\\#J_p$, respectively.
- `k-l-goebel_prime-integrality_1e3_img.pdf`: PDF file that includes the images in a format similar to Figure 1 in the manuscript. Each page represents the integrality status of each $(k, l)$ ($0 \leq k < p - 1$ and $0 \leq l < p$) for a fixed prime $p \leq 10^3$. Yellow and purple colors represent $pg_{k,l}(p) \equiv 0 \pmod{p}$ and $pg_{k,l}(p) \not\equiv 0 \pmod{p}$, respectively. 

## Codes
The actual codes have been written in Python.
The codes in files on the `codes_actual` directory were used to obtain the computational results in the actual run. Files are highly redundant and sometimes not very readable, but are included for archival purposes.

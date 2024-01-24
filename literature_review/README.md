## Literature Review on Private Information Retrieval (PIR)

<br>


We analyze recent advances on **Private Information Retrieval** (also known as **Homomorphic Encryption**) in the context of a **Story Protocol's hook for privacy, security, and compliance**.

<br>

----

### I. Introduction

<br>


#### What’s PIR

Private information retrieval refers to the **ability to query a database without revealing which item is looked up or whether it exists**, by using cryptography and zero-knowledge proof primitives. The concept was first introduced in 1995 by [B. Chor et al](https://www.wisdom.weizmann.ac.il/~oded/p_pir.html).


In a very simplified version of PIR on a matrix setup, **a client wants to retrieve the ith element `D_i` of a server database `D` (and `n` elements `D_i`), without letting the server know which element is being requested**:

<br>

<p align="center">
<img src="diagrams/pir1.png" width="80%" align="center"/>

<br>
<br>

#### Fully Homomorphic Encryption Schemes

To understand homomorphism, think of an example of a server that can `XOR` a client’s data. The client could send their cipher `c0`, obtained from their plaintext data `m0` and their key `k0`:

```
c = m0 ⌖ k0
```

Homomorphism comes from the fact that if a client sends two encrypted messages, `c1` and `c2` (from messages `m0` and `m1`, respectively), the server can return `c1 ⌖ c2` so that the client can then retrieve `m0 ⌖ m1`.

Partially homomorphic encryption is easily achieved as it can accept the possibility of not all the data being encrypted (or homomorphic) through other operations (such as multiplication). **Fully homomorphic encryption (FWE)** is achieved when a server operates on encrypted data **without seeing ANY content of the data**.

<br>

> 💡 *In a more formal definition, homomorphic encryption is a form of encryption with evaluation capability for computing over encrypted data without access to the secret key, i.e., it supports arbitrary computation on ciphers. fully homomorphic encryption is the evaluation of arbitrary circuits of multiple types of (unbounded depth) gates.*

<br>

In a [quintessential paper in 2005](https://dl.acm.org/doi/10.1145/1060590.1060603), Oded Regev introduced the **first lattice-based public-key encryption scheme**, and the **learning with errors (LWE) problem**. 

The LWE problem can be thought of as a search in a (noisy) modular set of equations whose solutions can be very difficult to solve. In other words, given `m` samples of coefficients `(bi, ai)` in the linear equation `bi = <ai, s> + ei`, with the error `ei` sampled from a small range `[-bound, bound]`, the problem of finding the secret key `s` is hard.

In the last years, research has been done to improve Regev's security proof and the efficiency of the scheme, including [Craig Gentry's 2009 first fully homomorphic encryption scheme](https://crypto.stanford.edu/craig/craig-thesis.pdf).

In the next sessions we review very recent advances on applying this theory, through an engineer (builder) point of view.

<br>

---

### II. "[One Server for the Price of Two: Simple and Fast Single-Server Private Information Retrieval", by Alexandra Henzinger et. al (2022)](https://eprint.iacr.org/2022/949) 

<br>

#### A Simple Single-Server Scheme as an Intuitive Illustration of How PIR Works

PIR schemes are generally divided into **single-server schemes** and **multiple-server schemes** (when you remove the trust of a subset of the servers). For this illustration, we will work with a vanilla setup for a simple single server, where **the “database” is represented by a square matrix whose elements are under a constant modulo**.

In the simplest setup, we have a server that holds an embedded database, and we have a client that holds an index `i` between `1` and `n`. The client wants to privately read the `ith` database item by interacting with a server following a PIR protocol, *i.e.*, without letting the server learn anything about the index i that the client is reading.

<br>

#### Possible applications of PIR

Possible applications that could use a PIR protocol once it becomes less expensive or prohibitive (*i.e.*, cheap computation with a small cipher, as PIR inherently has a high cost for server-side computation) are among:
- law enforcement
- safe browsing
- health providers
- banks
- stock exchanges

In the context of the Story Protocol, 

<br>

---



#### tl; dr



<br>

---

### III. Paper 2:

#### tl; dr




<br>









----

### IV. Closing Remarks

<br>

#### Gaps and Improvements


<br>

#### Impact to Story Protocol



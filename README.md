# ffi-overhead

This repo is modified from [dyu/ffi-overhead](https://github.com/dyu/ffi-overhead).

No [tup](https://github.com/gittup/tup) required.

Rust can be built with stable channel.

## Run

I didn't use makefile to reduce the required building dependencies.

```
./make.py -h
```

## Environment

My environment: wsl on windows 11

Intel i7-1185G7 (4 cores, 8 threads) with 16G RAM

- gcc: 11.4.0
- rustc: 1.79.0
- go: 1.22.5

```
$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

$ rustc --version
rustc 1.79.0 (129f3b996 2024-06-10)

$ go version
go version go1.22.5 linux/amd64
```

## Results

```
$ ./make.py run 1000000000
Running 3 files
> ./rust_hello 1000000000
968
> ./go_hello 1000000000
61434
> ./c_hello 1000000000
1399
```

package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {
	time.Sleep(100 * time.Millisecond)
	fmt.Fprintf(w, "hello\n")
}

func hello2(w http.ResponseWriter, req *http.Request) {
	time.Sleep(200 * time.Millisecond)
	fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {

	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}

func main() {
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/hello2", hello2)
	http.HandleFunc("/headers", headers)

	http.ListenAndServe(":8080", nil)
}

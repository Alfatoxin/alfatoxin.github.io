package main

import (
	"crypto/sha256"
	"fmt"
)

func main() {
	data := []byte("Sakarin Kaewsathitwong")
	hash := sha256.Sum256(data)
	fmt.Printf("%x", hash[:])
}

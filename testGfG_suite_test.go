package testGfG_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestTestGfG(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "TestGfG Suite")
}

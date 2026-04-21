package main

import "fmt"

type task struct {
	ID   int `json:ID`
	Name string `json:Name`
	Content string `json:Content`
}

type allTasks []task

var task = allTasks{
	{
		ID: 1,
		Name: "Task 1",
		Content: "This is the first task"
	}
}
package com.example.jetpack_compose_assignment_1



data class Course(
    val title: String,
    val code: String,
    val credits: Int,
    val description: String,
    val prerequisites: String
)

val sampleCourses = listOf(
    Course("Introduction to Programming", "CS101", 3, "Learn the basics of programming.", "None"),
    Course("Data Structures", "CS201", 4, "Study various data structures.", "CS101"),
    Course("Algorithms", "CS301", 4, "Focus on algorithm design.", "CS201"),
    Course("Database Systems", "CS401", 3, "Introduction to databases.", "CS201"),
    Course("Web Development", "CS501", 3, "Learn about web technologies.", "CS101"),
    Course("Introduction to Programming", "CS101", 3, "Learn the basics of programming.", "None"),
    Course("Data Structures", "CS201", 4, "Study various data structures.", "CS101"),
    Course("Algorithms", "CS301", 4, "Focus on algorithm design.", "CS201"),
    Course("Database Systems", "CS401", 3, "Introduction to databases.", "CS201"),
    Course("Web Development", "CS501", 3, "Learn about web technologies.", "CS101"),
    Course("Introduction to Programming", "CS101", 3, "Learn the basics of programming.", "None"),
    Course("Data Structures", "CS201", 4, "Study various data structures.", "CS101"),
    Course("Algorithms", "CS301", 4, "Focus on algorithm design.", "CS201"),
    Course("Database Systems", "CS401", 3, "Introduction to databases.", "CS201"),
    Course("Web Development", "CS501", 3, "Learn about web technologies.", "CS101"),
)
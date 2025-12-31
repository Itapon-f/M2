# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/27 00:00:00 by agiron-d          #+#    #+#              #
#    Updated: 2025/12/02 02:45:01 by agiron-d         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

SOURCES = 	ft_atoi.c \
			ft_calloc.c \
			ft_count_moves.c \
			ft_error.c \
			ft_execute_moves.c \
			ft_find.c \
			ft_has_duplicates.c \
			ft_putstr.c \
			ft_sort.c \
			ft_split.c \
			ft_stack_add_back.c \
			ft_stack_add_front.c \
			ft_stack_add_new.c \
			ft_stack_calc_moves.c \
			ft_stack_clear.c \
			ft_stack_do_moves.c \
			ft_stack_do_push.c \
			ft_stack_do_rotate.c \
			ft_stack_do_rotate_rev.c \
			ft_stack_do_swap.c \
			ft_stack_pos.c \
			ft_stack_remove_first.c \
			ft_stack_size.c \
			ft_strlen.c \
			ft_val_nbr.c \
			main.c

OBJECTS = $(SOURCES:.c=.o)

CC = gcc
CFLAGS = -Wall -Wextra -Werror -g
INCLUDES = -I.

all: $(NAME)

$(NAME): $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(OBJECTS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
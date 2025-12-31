# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itapon-f <itapon-f@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/22 18:21:51 by itapon-f          #+#    #+#              #
#    Updated: 2025/12/22 18:21:55 by itapon-f         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


NAME = push_swap.a

SRCS = 

OBJS = $(SRCS:.c=.o)

INCLUDE = ft_printf.h

CC = cc
FLAGS = -Wall -Wextra -Werror
LIB = ar -rcs
RM = rm -f

all: $(NAME)

$(NAME): $(OBJS) $(INCLUDE)
	$(LIB) $(NAME) $(OBJS)

%.o: %.c
	$(CC) $(FLAGS) -I$(INCLUDE) -c $< -o $@

clean:
		$(RM) $(OBJS)

fclean: clean
		$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re